
dog1 ={
    "name":'lai',
    "d_type":"j",
    "attack_val":30
}

#def bite(person_obj):
#    person_obj.life -=30


def dog(name,type):
    data={
        'name'=name,
        "d_type"=type,
        "life_val"=100
    }

    if type in attack_vals:
        data["attack_val"]=attack_vals[type]