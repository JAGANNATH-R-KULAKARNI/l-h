import requests

response =requests.get('http://apitoggle.eba-euvwme7s.us-west-2.elasticbeanstalk.com/list')
features=response.json();

# for feature in features:
#     print(feature["name"],feature["enable"]);

def GetfeatureByName(feature):
    for f in features:
        if f['name']==feature:
            return f.get('enable',False);

def GetfeatureBytag(feature):
    for f in features:
        if f['tag']==feature:
            return f;        
        
def GetfeatureByUser(feature):
    for f in features:
        if f['lastupdateby']==feature:
            return f;

def Isenabled(feature):
    for f in features:
        if f['name']==feature :
            return f['enable'];
            
print(GetfeatureByName("Feature8"));      
        
        
        