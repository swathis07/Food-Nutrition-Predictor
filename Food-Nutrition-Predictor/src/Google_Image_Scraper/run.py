


import settings

from fetch_resize_save import FetchResizeSave

if __name__ == '__main__':

    for i in range(41,100,10):
        search_params = {
            'q': 'pizza',
#            'hq':'ic:trans',
            'num': 10,
            'safe': 'medium',
            'fileType': 'jpg',
            'imgType': 'photo',
            'imgSize': 'large',
            'searchType': 'image',
#            'imgDominantColor':'yellow',
            'start': i
            }

        path_to_image = settings.IMAGE_PATH

        success, fail = FetchResizeSave(search_params=search_params, path_to_image=path_to_image,myiter=i).run()

        if success:
            # Do something with this new resized and locally saved image
            print(path_to_image)
        else:
            print(fail)
