#
# my_dic={"MobilePhone":""}
# key="MobilePhone"
# my_dic[key] = input(f"{key}: ")
# #my_dic[key] = str(my_dic[key])
#
# # Check if the number does not start with any of the valid prefixes or does not have 11 digits
# while not (my_dic["MobilePhone"].startswith("011") or my_dic["MobilePhone"].startswith("010") or
#            my_dic["MobilePhone"].startswith("012") or my_dic["MobilePhone"].startswith("015")) or len(
#     my_dic["MobilePhone"]) != 11:
#     print( "Mobile Number Must be 11 digits and Start with (010), (011), (012), or (015)"  )
#     my_dic[key] = input(f"{key}: ")
#     #my_dic[key] = str(my_dic[key])
#
# my_dic[key] = int(my_dic[key])


monum=input("Mobilt Number: ")
print(monum)