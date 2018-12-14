import re
import json
import itertools
if __name__=="__main__":
    #label_cypher
    # f=open("data/label.txt","r",encoding="utf-8")
    # list=[x for x in re.split("\n",f.read()) if x!=""]
    # print(list)
    # fw=open("data/label_cypher.txt","w",encoding="utf-8")
    # for i in list:
    #     s="CREATE(m:标签{实体名:\""+i+"\"})"
    #     fw.write(s)
    #     fw.write("\n")
    # f.close()
    # fw.close()



    # anc_cypher
    # fw = open("data/anc_cypher.txt", "w", encoding="utf-8")
    # f = open("data/result", "r", encoding="utf-8")
    # fc=open("data/anc_id.txt","r",encoding="utf-8")
    # anc_id_list=[x for x in re.split("\n",fc.read()) if x!=""]
    # count=0
    # while 1:
    #     count+=1
    #     line = f.readline()
    #     if not line:
    #         break
    #     _json = json.loads(line)
    #     if _json["anc_id"] not in anc_id_list:
    #         continue
    #     # print(_json)
    #     s="CREATE(m:主播{实体名:\""+_json["anc_name"]+\
    #     "\",主播id:\""+_json["anc_id"]+\
    #     "\",图标:\""+_json["anc_img"]+ \
    #     "\",声音数目:\"" + _json["anc_music_num"] + \
    #     "\",专辑数目:\"" + _json["anc_special_num"] + \
    #     "\",粉丝数目:\"" + _json["anc_fans_num"] +\
    #     "\",级别:\"" + _json["anc_rank"][1]+ \
    #     "\"})"
    #     fw.write(s)
    #     fw.write("\n")
    #     anc_id_list.remove(_json["anc_id"])
    #     if count%1000==0:
    #         print(count)
    # f.close()
    # fw.close()
    # fc.close()




    # al_cypher
#     fw = open("data/test.txt", "w", encoding="utf-8")
#     f = open("data/result1120", "r", encoding="utf-8")
#     count=0
#     while 1:
#         count+=1
#         line = f.readline()
#         if not line:
#             break
#         _json = json.loads(line)
# #         print(_json["resources"].__str__())
# #         print(re.sub("\"","\\\\\"",_json["resources"].__str__()))
#         obj = itertools.cycle(['“','”'])
#         _obj = lambda x: next(obj)
#         description = _json["description"].replace('\n','').replace("\\", "")
#         description = description.strip()
#         description = re.sub('"', _obj,description)
#         description = description.replace(' ','')
#         description = description.replace('\r','')
#
#         s = "CREATE(m:专辑{实体名:\"" + re.sub(r'"', _obj, _json["name"]).replace("\\", "") + \
#             "\",id:\""+re.sub('"', _obj, _json["id"]).replace("\\", "")+\
#             "\",描述:\""+description+ \
#             "\",图标:\"" + re.sub(r'"', _obj, _json["img"]).replace("\\", "") + \
#             "\",资源数目:\"" + len(_json["resources"]).__str__().replace("\\", "") + \
#             "\",列表:\"" + re.sub(r'"', _obj,_json["resources"].__str__()).replace("\\", "") + \
#             "\",点击量:\"" + _json["operate_time"].__str__().replace("\\", "") + \
#             "\",最新更新时间:\"" + _json["update_time"].__str__().replace("\\", "") + \
#             "\"})"
#         fw.write(s)
#         fw.write("\n")
# #         if count==10000:
# #             break
#         if count%1000==0:
#             print(count)
#     f.close()
#     fw.close()

    # anc_al_relation_cypher
    # fw = open("data/anc_relation_cypher.txt", "w", encoding="utf-8")
    # f = open("data/result1120", "r", encoding="utf-8")
    # count = 0
    # while 1:
    #     count += 1
    #     line = f.readline()
    #     if not line:
    #         break
    #     _json = json.loads(line)
    #     s = "MATCH(n),(m) WHERE n.id=\""+_json["id"]+"\" and m.主播id=\""+_json["anc_id"]+"\" CREATE(n)-[:主播]->(m)"
    #     fw.write(s)
    #     fw.write("\n")
    #     if count % 1000 == 0:
    #         print(count)
    # f.close()
    # fw.close()



    # label_al_relation_cypher
    # fw = open("data/label_relation_cypher.txt", "w", encoding="utf-8")
    # f = open("data/result1120", "r", encoding="utf-8")
    # count = 0
    # while 1:
    #     count += 1
    #     line = f.readline()
    #     if not line:
    #         break
    #     _json = json.loads(line)
    #     if _json["tags"]!="[]":
    #         tags_list_middle=[x for x in re.split("(\[\\\"|\\\"\, \\\"|\\\"\])",_json["tags"])
    #                           if x!="" and x!="[\"" and x!="\", \"" and x!="\"]"]
    #         for i in tags_list_middle:
    #             s = "MATCH(n),(m) WHERE n.id=\"" + _json["id"] + "\" and m.实体名=\"" + i + "\" CREATE(n)-[:标签]->(m)"
    #             fw.write(s)
    #             fw.write("\n")
    #     if count % 1000 == 0:
    #         print(count)
    # f.close()
    # fw.close()


    #voice_cypher
    # fw = open("data/voice.txt", "w", encoding="utf-8")
    # f = open("data/result1120", "r", encoding="utf-8")
    # count = 0
    # while 1:
    #     count += 1
    #     line = f.readline()
    #     if not line:
    #         break
    #     _json = json.loads(line)
    #     #print(_json['resources'])  #列表
    #     obj = itertools.cycle(['“', '”'])
    #     _obj = lambda x: next(obj)
    #     if _json["resources"]  == None:
    #         continue
    #     for _voice in _json['resources']:
    #         # print (_voice)
    #         s = "CREATE(m:声音{实体名:\"" + re.sub(r'"', _obj, _voice["res_text"]).replace("\\", "") + \
    #             "\",收听数:\""+_voice["res_opreat_num"].replace("\\", "")+\
    #             "\",发布时间:\"" +  _voice["res_time"].replace("\\", "") + \
    #             "\"})"
    #         print(s)
    #     fw.write(s)
    #     fw.write("\n")
    #     # if count==10:
    #     #         break
    #     if count % 1000 == 0:
    #         print(count)
    # f.close()
    # fw.close()



    # resource_voice_relation_cypher
    fw = open("data/voice_relation.txt", "w", encoding="utf-8")
    f = open("data/result1120", "r", encoding="utf-8")
    count = 0
    while 1:
        count += 1
        line = f.readline()
        if not line:
            break
        _json = json.loads(line)
        # print (_json)

        for voice in _json['resources']:
            s = "MATCH(n),(m) WHERE n.id=\"" + _json["id"] + "\" and m.实体名=\"" + voice['res_text'] + "\" CREATE(n)-[:包含]->(m)"
            fw.write(s)
            fw.write("\n")
            # print(s)
        # if count==10:
        #         break
        if count % 1000 == 0:
            print(count)
    f.close()
    fw.close()