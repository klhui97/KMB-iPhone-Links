import requests
import json
import datetime

buses = ['237A', '87S', 'E41', 'N603', '249M', '38P', '215P', 'A31P', '31P', '272S', '116', '14B', '276A', '40P', '70S', '89P', '111P', '42M', 'R603', '17', '103', '270P', 'N30P', '673P', '914', '278X', '78K', '243P', 'N290', '68A', '168R', '49P', '282', '240X', '302', '18', '273C', '606A', 'A41', 'A32', '978', 'R968', '83A', '215R', '276B', '271P', '269R', '270C', '36B', '16M', '936', '72X', '203C', '117', '249X', '69C', '107', '2F', '272A', '66X', '224R', '14H', 'E32A', '42A', 'N30S', '113', '276', '81K', '273', '290A', '36A', '273B', '46X', '606X', '95', 'S64C', '118', '81S', '1', '80X', '73', '205M', '234B', '948A', '30', '74C', 'W2', '678', '82P', '980X', '89S', '41P', '272E', '74D', '271S', '86K', '619X', '98P', '14X', '85X', '98C', '69X', '261P', '270A', '215X', '5M', '6C', '283', '258D', '848', '51', '68E', '38A', '91S', '259X', '224X', '171A', '281M', '272X', '30X', '75K', '80', '260X', '263A', '5D', '891', '71B', '93M', '68R', '106P', 'E31', '296C', '87P', '269B', '914X', '101X', '178R', '91M', '893', '2', '603', '277P', '106A', '960P', 'E32', '301', '261', '278A', '601', '11', '284', '673', '203S', '89B', '80K', '32P', '43P', '238M', '60M', 'N368', '275R', '41A', '58X', '86P', '948X', 'N39', '270R', '34M', 'N281', '64K', '259C', '254R', '269C', '43X', '936A', '960B', '214', 'E33P', '286P', '281A', '28B', '72A', '681', '7B', '263', '49X', '32', '12', 'N118', '72C', '7M', '307', '23', '82B', '273P', '6P', '80M', '680', 'N601', '66M', '15X', '57M', '621', 'NA30', '38', '115', 'N170', '11X', '59A', '681P', 'X42C', 'N252', '67M', '105R', '71K', '79K', '85S', '234A', '61X', '87K', 'R960', '272P', '273D', '690P', '261B', '102R', '241X', '63R', '603P', '213S', '934A', '82C', 'N31', '16X', '290X', '13X', '270', '271X', '606', '270S', '43A', 'N307', '13P', '216M', '251B', '613', '87D', '1A', '46', '59M', '961P', '89', '5X', '23M', '74S', '76S', '276P', '968', '259E', '208', '31M', '85M', '76K', '982X', '58M', 'A33P', 'N73', '269M', '258X', '869', 'S64P', '287X', '61M', 'NA31', '73A', 'N237', '182X', '43M', 'R108', '6R', '45', '103P', '601P', '91P', '603A', '48X', '293S', '268X', '872', '960X', '11D', '274P', '73X', '948B', '27', '35X', '53', '74X', '47X', '234C', '54', 'N171', '297', '948P', '3C', '68F', '107P', 'N42A', '40S', 'NA40', 'N41X', '98S', '248M', '203E', '71S', '74B', '71A', 'X42P', '288A', '5A', '93K', 'E33', 'X41', '980A', 'N373', '95M', '81', '235M', '258P', '267X', '58P', '40X', '273S', '265B', 'N269', '264R', '978B', 'N182', '292P', '299X', 'X90', '968X', 'N680', '238P', '260B', '259D', '219X', '52X', '74A', '960', 'NA43', 'X89D', '268P', '307C', '302A', 'T277', '29M', '260R', '281B', '38B', '104', '31', '72', '960C', '251M', 'A37', '38S', '42R', '47A', '2D', '13M', '234X', '270D', '251A', '11K', '68X', '243M', '68M', '680A', '85A', '32S', '70K', '89R', '261X', '86', '13D', '21', 'A33', '296M', '914P', '230X', 'N121', 'N36', '619', '101R', 'N287', '41', '286M', '2B', '75P', '67X', 'R78', '36M', '269P', '80P', 'NA32', 'E34X', '110', '10', '5C', '960S', '213X', '288B', '89D', '269A', '37', '99', '6', '74K', 'R33', '278P', '280X', '213A', '281X', '88X', 'A31', 'E32P4', '258S', '87B', '85K', '279A', 'X33', '98A', '39M', '74P', '6D', '3X', '296P', '373', '65K', '277E', '60X', '98D', '170', '40A', '641', '68', '41M', 'N243', '271B', '8P', '83S', 'X1', '889', '279X', '15', '3D', '277X', '87R', '36R', '258A', '252', 'NA37', '62X', 'N42P', '12A', '43', '234D', '14', '11B', '83X', '84M', '87E', 'N106', '106', '31B', '868', '118P', '961', '96R', '619P', '112', '252B', 'N241', '985', '41R', '268C', '968A', '259R', '273A', '269S', '298E', '286C', '85B', 'NA47', '288', '26M', '3B', '83K', 'A43', '5', '270B', '46P', '48P', '64S', '73B', '111', 'E34A', 'A33X', 'K17', 'N216', '35A', '93A', '94', '16', '235', '86C', 'S1', '42', 'NA33', '89X', '234P', '117R', 'N122', 'S64X', 'N30', '43B', '39A', '82K', 'N619', 'NA41', '88', '286X', '8', '213M', '265S', '88K', 'R8', '73K', '260C', '297P', '290B', '69P', '2E', '14D', '91R', '5P', '40', '935', '75X', '274X', 'K12', '289K', '101', '211', '271', '77K', '307A', 'N64', '680B', '98R', '3M', '102', 'A41P', '242X', 'N42', '81C', 'K18', '32H', '272K', '290', 'N293', '36', '59X', '85', '680P', '278K', '44M', '2A', '904', '8A', 'B1', '888', '92', '981P', 'N3D', '63X', '86S', '43C', '42C', 'N271', '44', '211A', '948', '7', 'N283', '102P', '905', 'A43P', '109', '213D', '28', '296A', '15A', 'T270', '182', 'NR', 'N691', '934', '26X', '14S', '603S', '203X', '5R', '2X', '238X', '33A', '43D', '36X', '11C', '34', '69M', '960A', '99R', '905P', '26', 'N260', '296D', '268A', '115P', 'R42', '271R', '108', '680X', 'E34B', 'E42', '690', 'A47X', '91', '268B', '171', '28S', '89C', '671', '307B', '6F', '171P', 'R961', 'S64', '307P', '3S', '82X', '252X', '9', 'K14', '269D', '265M', '978A', 'N673', '86A', '80A', 'N116', 'NA34', 'W3', '37M', '24', 'A36', 'X34', '259B', '74E', 'E34P', '32M', '872X', '274']
buses = list(set(buses))
print(buses)
links = []

def addToLinksIfNeed(r):
    try:
        result = json.loads(r.text)
        items = result.get('response', {})
        for item in items:
            link = item.get('rsa_exthttpurl', '')
            if 'luckdraw' in link:
                links.append(link)
                print(link)
                # r = requests.get(link)
                # print(item.get('rsa_exthttpurl', ''))
    except:
        print("fail")
    

def main():
    for bus in buses:
        r = requests.get('https://app1933.kmb.hk/kmb_v2_webservice/api.php?lang=tc&version=3&platform=ios_12.1.2&deviceid=672815fc1d196fd5234621234ab313f7md&model=iPhone10,2&rand=1548069114&action=getbusstopad&route_bound=' + bus + ',1')
        addToLinksIfNeed(r)
        r = requests.get('https://app1933.kmb.hk/kmb_v2_webservice/api.php?lang=tc&version=3&platform=ios_12.1.2&deviceid=672815fc1d196fd5234621234ab313f7md&model=iPhone10,2&rand=1548069114&action=getbusstopad&route_bound=' + bus + ',2')
        addToLinksIfNeed(r)

    text_file = open("index.html", "w")
    # text_file.write("最後更新: " + str(datetime.datetime.today()) + "</br>")
    for link in links:
        text_file.write(link + "\n")
        # text_file.write("<a href=\"" + link + "\" target=\"_blank\">" + link + "</a></br>")

    text_file.close()

main()