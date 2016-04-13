import os
import shutil
import requests
from PIL import Image
from resizeimage import resizeimage

import settings
from google_api import GoogleCustomSearch
import tempfile


class FetchResizeSave:

    def __init__(self, search_params, path_to_image, myiter):
        '''
        PARAMETERS:
        search parameters,
        directory to save images,
        number of iteration
        '''

        self.search_params = search_params
        self.path_to_image = path_to_image
        self.myiter = myiter
        self.google_custom_search = GoogleCustomSearch()

    def run(self):
        '''
        INPUT: None
        OUTPUT: Return bool to indicate success or failure
        '''
        image_from_google, google_exception = self.google_custom_search.photo_from_google_images(**self.search_params)

        if not image_from_google:
            return False, google_exception
        else:
            dir_to_image = '/'.join(self.path_to_image.split('/')[:-1])
            dir_to_image = os.path.join(dir_to_image,self.search_params['q'],str(self.myiter))
            if not os.path.exists(dir_to_image):
                os.makedirs(dir_to_image)

            for i,image in enumerate(image_from_google):
                print (i, image)
                req = requests.get(image, stream=True)
                if req.status_code == 200:
                    path = os.path.join(dir_to_image,'image_'+str(i)+'.jpg')
                    with open(path, 'wb') as file_on_disk:
                        req.raw.decode_content = True
                        shutil.copyfileobj(req.raw, file_on_disk)

                ## Resizing and saving image
                fd_img = open(path, 'r')
                img = Image.open(fd_img)
                try:
                    img = resizeimage.resize_cover(img, settings.IMAGE_SIZE)
                    img.save(path, img.format)
                    fd_img.close()
                except Exception, e:
                    print e
                    continue

            return True, None
