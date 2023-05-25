# Get file name
name = input('File name: ').lower().strip()

# Get file extendion
extension = name.split('.')[-1]

# check file extension and return result
match extension:
    case 'jpg' | 'jpeg':
        print('image/jpeg')
    case 'gif' | 'png':
        print(f'image/{extension}')
    case 'pdf' | 'zip':
        print(f'application/{extension}')
    case 'txt':
        print('text/plain')
    case _:
        print('application/octet-stream')

