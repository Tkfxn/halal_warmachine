
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()

# Force offline access and re-prompt
gauth.GetFlow()
gauth.flow.params.update({'access_type': 'offline'})
gauth.flow.params.update({'approval_prompt': 'force'})
gauth.LocalWebserverAuth()

gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in file_list[:10]:
    print(f'{file["title"]} ({file["id"]})')
