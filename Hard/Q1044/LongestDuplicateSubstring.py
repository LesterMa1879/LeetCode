import collections
from itertools import groupby

# IMPORTANT QUESTION!!!
# the suffix tree

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        d2 = collections.defaultdict(list)
        d = []
        skip = 0
        for x in range(len(s)):
            d2[s[x]].append(x)
        for _, l in d2.items():
            skip = max(skip, max(len(list(g)) for _, g in groupby(enumerate(l), lambda a: a[0] - a[1])))
            d.append(l)
        if skip > 3:
            visit = skip-2
        else:
            visit = 1
        while visit < len(s):
            d2 = []
            for v in d:
                if len(v) > 1:
                    d3 = collections.defaultdict(list)
                    if skip > 3:
                        for k, g in groupby(v, lambda a: s[a: a+visit+1] if a+visit+1 <= len(s) else "~"):
                            d3[k] += list(g)
                    else:
                        for k, g in groupby(v, lambda a: s[a + visit] if a + visit < len(s) else "~"):
                            d3[k] += list(g)
                    for k, g in d3.items():
                        if k != "~" and len(g) > 1:
                            d2.append(g)
            if len(d2) == 0:
                if visit == 1:
                    for v in d:
                        if len(v) > 1:
                            return s[v[0]]
                    return ""
                return s[d[0][0]:d[0][0] + visit]
            d = d2
            skip = 0
            visit += 1
        return ""


s = "vbaemlrfvasubbuxdqohlpkuuznigzebcegorztmbngdocautqbegnbamqitrowtucjldexfsgiiiicbyeigrjjgbtbsiznccwohanmutudceffflnlfywnbqotypictesbhgndbkgfooltzahgbdtctjytzgwsnotwwhzyrifhwqbxtkewnxyjhycgfaauruqpbrnuztbxlevgobccydnhbppisqelmuapoqjnlmnyrkfflhjlkwvookwgcbtoxtdnlobwbqvsaazljjywftktgibiluzlqeybtbawrxqtzpeiyfggysbebdpozozpuatpbvlvsbortvbtaizaabfbgushkrxgtswvnhqflgyebzzdhzeicllkhdrrxqxqivnxdfeqmcupctvluztykhirmcklsjcdfrckxhallwcprxboywmidxbqbnbtzfygzbqyksjvqnljloxjkmuolxgmljhmrgsqjkovezqwmdfxrfjctfsecaspjzbahvqsfgnlfghsjnrduchnhzrkzlbkkdnuyfogmcrrkzltofyihfvpgobhzcslffhgkwowafqkgdduieeqjbhqpixqkrcswlajhohhvxrcdxylbfdmgkeyueohvsbuebdlrkvmkmonlpaougbashynlpujhvdnyizpuwdgiuvwjwkfenfwvgjixfrgcwuaevrbrvhbpdxabkffxmduundrswyxtszznrceomffpfhspmzoycltrqmmmkjhcijrblvrxdyokfibrjrsmcndszrhkaqolzgmndgkiebuklvdvnvhrkmmkgvuglkrlqgaummesnzczwiujfddqrraxmwgxgzkxfkttxzmkyqlvyhggmlwecwdoujoajyzqjukiuyuuogrppavcntiqrnglzunkvnagjmofmicbqtsgvpkjiubzhhmiezszovfahvfudjxufrcaiolqimrrufaaguzvpgxxbetgosctlgvtuhletcwpjyppsqmiyjhbocicukxhrsanzlsvpqkyocniucqtlzubbefxpceixexwpprgheevgueawwvhwqjzuqxltdvqitozkigsmmpugvwcssmqkxpgnouispyckpbvxjplwehcadhuxtmjqbsdqmmkdmmqdpnazcnxiubkaiezbqlrudxmrjwwximbzzbydrxmlzwnhdnjtycpdzbukxsihfjjgmhmdfyrgwgnztyvtdkwcmspllxvsgeaunmaumrajzqivofotqnwehlrskomsunmkzmemfhxfxfannqhfdfllsefctsuphgzgvguanrfmzhzmyitdneqfiwjdqdtzmufhachntpzuwbgwjbazfqgqoqtgtofhjnojpwzknafldnippkowcwmtmiziwhphuetlcsxruecyumnlwdhbzwuoevwccnkytdlxxjorptrjfeuehcfhabvewtizguzczlzwwqqljhxqmruvvbcvczbbsmcbgbfgoeemwuyfexwqosnmwqjyrnbmzdpffunvasixmieqfcivvwhrotrhgvtfyimfcabfsjcgtgxyjhvgffztysbenwlmhxtjxuopfswybvykeuskztdzlgdbfonmngxldocigajhxhtcdnmegrdsagvfwirkqqxvebelcpubwqdcdpgmjkgjsbqpjjbbzaxebdrfsnhqdksjcbvlnbwfcmwnxxqwxpcbstgmjndmaxxcaspnvntzzpmypfuouxrpsybblgqlgnpgiewdtpdsgrsxynovmfkefnirwyecnukvaibuzeoixhfywvtiddmiqwbmugqicddcleylkptkwaiswbcbgqjynlnhtfrvixzwdyhonaalckfalhbtxnrkagutmlowipsmnzccbepeouebdiubvnnvwjqiveefvxtlyxnabfgpzmqdwmgrcvoyfegckmhgldrkagmelutnimsfyyyctnaaticgvkmipfuplgtzcpmlbeqbeoezdgaxpcdmmrudwrtjxoicdwngadketqexwewnizbxsyaqptzokkqpgdwhginaytzwzvmiwnfolfeabfplpfawlydristimsflprtleazsgfshljucrwycvdvfwrokltvbmrmsrokzvfgiqalhzjlwnhblapvlksmyjbrdpdcmklvbngkmrwiefkrfbmqoffmqgfvxlyjvjgyymllghtkofevjqnxxslqarlzejlzuratglemuzyihcfqvspslaintunxfyzapzvxmbjgaiqjmvbhpqactkqmgdmmdloumlsamdionyyavzhksjnlwdzcilqnyghmrzmdfussussrrccjlrwjwwoehetilauecjkhfczcuutnwvzjmvtirhobnhjakffmqpvwtwypqrcmpdwdzrosycvlmgoymtmckhaddaswswijagmbxatxfpltvzrjudoemohppznjxwsxegaehudmlofipyujbinnywepxsavqsuwzvaireweudombixeslrtjxihrjehdyeetgommkqjpfvqpsuifnbrnlyewcoccuiycxkpjbyzivrxpohvbkmqwmxuqlwshfqjedyngymotenjsvgvfuodilyyywqfbjofmpvsnhijnvufscdayrdgcdeaawhdhxltmgncnvndtjkllnllerriuxkwvtadrnydtmhijulcdwoolbzsssaprnlngnsxaqdvekeqfrsinizzkarevttmihzpwrozkruqcagjszthjsitvbaqxtcfcewzxlajeuaixgrrhlarfjmammsjivrkbnlyalihikphqjyywyrbjdewqwhytykuowvqjfxtppahaahwzyzkcdgscqsvocseapxmuwfllisniajjajucocwqsoojtgnvvmhrjpcwxwkhyvrzgnbvpaniqbtjjihevqxefbaeymoyihxoubljbztrcodmxmsscqwktyqrnesvlplhsxtvyopadumaghskxquqqnkdreafvmmolhjjwylzuazahtlgjhybukfoohvktjygrjpnkbmednhkgsqrbosyzzopjjzcszjllaaxdobgbkqjeiagzvgawupfdrkxqvjdvlabaehboaltknbjihjhbbmgswdkroopaoqauzdjboeoehxoojvpmkvegaoaperrvjrpkwamlgcrnzfbkbswlpctstvjxmauxtkipmwctytizzmkcgipwnkqgizfwzausmcjaymvwheviqhkwsbufoknwlssksmegqohqccojgmsytexnirswehspamcubibryiiamwmvketekqtskooqvihvvjswutpsdztryfmilgmvyiokwcarnkpivhgpcvihvdytklbvrqsrygcwlenyqeimlodpjnweqvzagbxztqsrywnlbcjthtfuhjktwgxpdzrjarkvjdmhzbtcfewmydjhmtalbacfztqbmbwvgkdhlykseghejqmylmlmmptnkkoxnmstwxajvmccujggbsgmhtaviujsgzptmiokfqudfyfzjnfkgnwpgwkosvjyvytjihtqaptfnaewnmivzekgdxwxsfwnepyozsebhzgxzmtnackaivinselmmjcsyagzslackgzmvubvylxhifwcmhpyqrqrrwsmjtqwbriwljukurtdzrhlzwjrpbkjzdvjwnfzenyrysdslwxkofvpdgitjtcjwzsumztsotjmlpexnejdlfsondjxwlgumaoabjspdebqvhpilzmygenvjysfkazycpzdbtsgztwubmdonpnvvcqfajmmlolodmrgfmmhfjbixgxmxkhtmxamiobucmkiydofpdmvoqdnwczumipyfpnqfokicwsczihplwmzmrmiunegvthdkwtqmfaobsqcczroxfpjxeuttybpskucgnussuivoaxrarhzwwlvcfqwfslxcfcluydotmljmiaobhoagzxigoelirlmypxsndiiptsdcuufekfkldurtbcbupntennsqwchrukvrgbvqghbldseexhzovutijnahphzmrudyvyqefspimwpldqaaktkvikdxrcjlymlwkbartrcinrttjttvoeqwovuixftyseuehuydnaldtewcarxovplmlhukmpietclayjfmjqpexnixehlcwyojfkuszeyuhlwfuctfuijrvtocacexauiigcafhabqmzxidroybzpxtgztifskzbsffumovpejoeruvhswhjvcpwxzbskcvcjazvrwmxhdbyxwirvraqtsnqrqidtdieghaxfowmrykowufrlikeazxtphzknhpvqruvfqhxotnlovczdogfnfadozpbggwwxstfjaexutkiopjtdrarwbwlalojunhtfbyobeoxyyhmnririikfjgsmtgvntehbfhpjmdgmeoyrhikpruwcaqqwxnjssstzcliqqrcufcoolydcvcgxsxtrkfkexfezqmrjdtdkwryhselnitmaqgsdlehkjnkccblhxqutksacynrggdjxldcwhlhsbtwdwhktyemizomzbfikkrjwuludydxzwucvbpobtdlutzuvgcfrvqprblubptblnfgruxuqagmvhgqokxhhnyyqjuuyovmbcsuxrpptxbpekhuwhdewbcplzjjpevsiqnfjcwdzaufkbcgifkfjpuuqfffjdxrvmzeoxjpxdxhfzqpgcwptqljvrqgwoarabvrahiykfhpgxhpcdevwshtlxchlcyofvffcnfpvngbmnsqrzmnrtgcqkjemjstezzjmgyjtgniufynemavfizytichtubavcjhijtepgollmyqzangjneexgnrcqrxuchfncjcizqtlolmpbtaozenitemkxmebvjoxutftjyhxmtmnoodqsqyoxkywycytomqifvcowjokeaxvpaljsjxpvxoucmpqygaebcuznijulipckandlnugkicousevafbdjvdzgottxivhikmtxjbkrgyoyfjykmbvhgupvniuxfdfqqapzczsiagifrirdlmnsjepwnjwsmbkeeadizysbgagaixftmsnvxctmlpeatrexrkfsixuqzaqhawcmqshpuabiqiijzmisynkikezjhrshpwvgocxleztujbfkpncocmwotxzaptjeqemgikrmlkjulqedggriupxpnwrcqaiigxoqhidssoogeujmcavwrumesdiigrsoojfxrirlyhrebardcmbugnaytjjzcdnsmupfeircpihslavpmwlummuhxfgzjvtxskdwsuzjeibriyhwwusiimpfsxgdvzcnjflbbkmgunxengakbssjhkrbjxeexitgofkrrwxomxszfvjgnesuqjxzgbgdkzmagwraurogqiivdterxwnphlpnovtawhcffufznviddqyhjcajanyhapxpksrjzuoeqvfdqngvfgcpjeajuatusqlckdnjzdppyuuqiamngqervgdpjwlboxfyctjdwysxuopcobswuyqrhtgqrtrhswhurqzqqtpkhepvgjuchktofbgyuxfnwmjpejhuewgmbxjjgdlqpgguhnsdmzsklccrnjnriufjrpuashsknyeunzzcysokwsdjercmlixezrgtyydnzijohisfajrwdxhhomvzwsfvlmolmsylchclqwssfkpjjyqxkmyigdfsrudeoerqlvbdstwxfnionbnanlivpopiktmazgqkbtqtootwbbmqcaqrlzncpclbxzbwhtjlmbecpzysbnidnzxaamdrqqsorvmboxmcasepsfjtssyhtxhvjmoaegqydezrcntcfzuxedsyxrfsoppaddailqioujfywadbazzgethekowbdmdjrdtdvbrrkzsgzvhbwiiacreofdrlruuiznluofmyeggfdphzyrbciisplkaceukehyaxdovjudoxtxwtqavyinqtzqxglhksfmqkbntvtkvmhtfytcybrowrhtzsdjmixevysowlarzikgigkihbzgugztacemncriclyywzrxjcdtkndrqczlkzgkdnxqpqatbzuzalwlpzezohtemsrytylxlkpcaqxbrrardycsxiunrnrffjebjpywznabdxcwpenucrobbiotvhadseebvezwrzxxzztqfjkhcykgjabgibjagpedvdanfxmexhuesemxeydnzeuhffjnxntstthyqvcpdwuxciuigxyfdsolzyayntrgmaefwiubeqyiytrhspmwjdjkdjjqdcxrcdwamrbshabivupnldlwguglercjvbaaexasoclxeofzkumxyytgubsyvwhqxiqdhtwvvjszzaalumiumbdjevhzrrsqbktidrfaczbdzbowqwsezvngsxflozbrkxbpqgqvhryhtnfjlzplvdrpaybqyejkbkzusrpzjnieapnmpczkhqzhqczqhiciscckvrmehuijkxvzcwljomtfpsvwbygtclgxeselomvamsbormxfbqksliqmiwhmjplojpbyeyyqtcekqdprwcjhmzvuycihstxbjbbnbcduejgumwmkaxrmzmgzroijhgmsjohksmhwvnqkleulemxdafcrtkcdsrxdffqzrxvnmnzyutjyhhdimhbitenovkrcrjbjgyyvnxthsehalkkatlknrxdmjwqbgtmmtkhhjcobhwduinuczgrqdufpqxqwtclmoutzzkcgigaqtxuudlnjhsyarqykulxkgsjfclnmtpdnozjslwduqduitvupgrzmmitqvidpyiemhngumlpcolmjghynaxbmfxfdfisfsyuzncuzojccwqmdxkqyitmpqrsybmftkzvycpzqaduwugbttttbngsfznddzjymktmmklekpzjlfkeyeybtgwyhjcmknlwxgkmryqdppmavxevdezwmvuueygqntplazxtxnwmfjocivxlzyhotdizeqqrkfcmgbferbswkhysexffwotrsbrwuhneossuvxamavklekfiknnibhztkqrezfipzckuzmjahvnliuvshjclsbecuyhtdrleuvatjjvrhkepfajollzdmgfgemcjeppampvvzrmibtxivgxgtyjfeookdsvjhkjtaeobvdjzyghtogzhfiolyewbyrkfcvaearfxwowuwgnmmovrwldwszyqskwwgyaiphflxehvkwjwkeqistfkufaorylxxnhovncutjqdgzbsgrbamimgnmxeniemxlauaepvqhyyicqottqibcqqrnxevdqvqsprzgopnnnwrdmmxfuahlryyoewtwrjricqprfcguaxzpjwuezbpqcpgglzdckunnkcereklhhkwsjqwirnavficqjfvtziglkkeqwrzfdvymnwwhmycrgejrjelkorxaebtcssivbaemlrfvasubbuxdqohlpkuuznigzebcegorztmbngdocautqbegnbamqitrowtucjldexfsgiiiicbyeigrjjgbtbsiznccwohanmutudceffflnlfywnbqotypictesbhgndbkgfooltzahgbdtctjytzgwsnotwwhzyrifhwqbxtkewnxyjhycgfaauruqpbrnuztbxlevgobccydnhbppisqelmuapoqjnlmnyrkfflhjlkwvookwgcbtoxtdnlobwbqvsaazljjywftktgibiluzlqeybtbawrxqtzpeiyfggysbebdpozozpuatpbvlvsbortvbtaizaabfbgushkrxgtswvnhqflgyebzzdhzeicllkhdrrxqxqivnxdfeqmcupctvluztykhirmcklsjcdfrckxhallwcprxboywmidxbqbnbtzfygzbqyksjvqnljloxjkmuolxgmljhmrgsqjkovezqwmdfxrfjctfsecaspjzbahvqsfgnlfghsjnrduchnhzrkzlbkkdnuyfogmcrrkzltofyihfvpgobhzcslffhgkwowafqkgdduieeqjbhqpixqkrcswlajhohhvxrcdxylbfdmgkeyueohvsbuebdlrkvmkmonlpaougbashynlpujhvdnyizpuwdgiuvwjwkfenfwvgjixfrgcwuaevrbrvhbpdxabkffxmduundrswyxtszznrceomffpfhspmzoycltrqmmmkjhcijrblvrxdyokfibrjrsmcndszrhkaqolzgmndgkiebuklvdvnvhrkmmkgvuglkrlqgaummesnzczwiujfddqrraxmwgxgzkxfkttxzmkyqlvyhggmlwecwdoujoajyzqjukiuyuuogrppavcntiqrnglzunkvnagjmofmicbqtsgvpkjiubzhhmiezszovfahvfudjxufrcaiolqimrrufaaguzvpgxxbetgosctlgvtuhletcwpjyppsqmiyjhbocicukxhrsanzlsvpqkyocniucqtlzubbefxpceixexwpprgheevgueawwvhwqjzuqxltdvqitozkigsmmpugvwcssmqkxpgnouispyckpbvxjplwehcadhuxtmjqbsdqmmkdmmqdpnazcnxiubkaiezbqlrudxmrjwwximbzzbydrxmlzwnhdnjtycpdzbukxsihfjjgmhmdfyrgwgnztyvtdkwcmspllxvsgeaunmaumrajzqivofotqnwehlrskomsunmkzmemfhxfxfannqhfdfllsefctsuphgzgvguanrfmzhzmyitdneqfiwjdqdtzmufhachntpzuwbgwjbazfqgqoqtgtofhjnojpwzknafldnippkowcwmtmiziwhphuetlcsxruecyumnlwdhbzwuoevwccnkytdlxxjorptrjfeuehcfhabvewtizguzczlzwwqqljhxqmruvvbcvczbbsmcbgbfgoeemwuyfexwqosnmwqjyrnbmzdpffunvasixmieqfcivvwhrotrhgvtfyimfcabfsjcgtgxyjhvgffztysbenwlmhxtjxuopfswybvykeuskztdzlgdbfonmngxldocigajhxhtcdnmegrdsagvfwirkqqxvebelcpubwqdcdpgmjkgjsbqpjjbbzaxebdrfsnhqdksjcbvlnbwfcmwnxxqwxpcbstgmjndmaxxcaspnvntzzpmypfuouxrpsybblgqlgnpgiewdtpdsgrsxynovmfkefnirwyecnukvaibuzeoixhfywvtiddmiqwbmugqicddcleylkptkwaiswbcbgqjynlnhtfrvixzwdyhonaalckfalhbtxnrkagutmlowipsmnzccbepeouebdiubvnnvwjqiveefvxtlyxnabfgpzmqdwmgrcvoyfegckmhgldrkagmelutnimsfyyyctnaaticgvkmipfuplgtzcpmlbeqbeoezdgaxpcdmmrudwrtjxoicdwngadketqexwewnizbxsyaqptzokkqpgdwhginaytzwzvmiwnfolfeabfplpfawlydristimsflprtleazsgfshljucrwycvdvfwrokltvbmrmsrokzvfgiqalhzjlwnhblapvlksmyjbrdpdcmklvbngkmrwiefkrfbmqoffmqgfvxlyjvjgyymllghtkofevjqnxxslqarlzejlzuratglemuzyihcfqvspslaintunxfyzapzvxmbjgaiqjmvbhpqactkqmgdmmdloumlsamdionyyavzhksjnlwdzcilqnyghmrzmdfussussrrccjlrwjwwoehetilauecjkhfczcuutnwvzjmvtirhobnhjakffmqpvwtwypqrcmpdwdzrosycvlmgoymtmckhaddaswswijagmbxatxfpltvzrjudoemohppznjxwsxegaehudmlofipyujbinnywepxsavqsuwzvaireweudombixeslrtjxihrjehdyeetgommkqjpfvqpsuifnbrnlyewcoccuiycxkpjbyzivrxpohvbkmqwmxuqlwshfqjedyngymotenjsvgvfuodilyyywqfbjofmpvsnhijnvufscdayrdgcdeaawhdhxltmgncnvndtjkllnllerriuxkwvtadrnydtmhijulcdwoolbzsssaprnlngnsxaqdvekeqfrsinizzkarevttmihzpwrozkruqcagjszthjsitvbaqxtcfcewzxlajeuaixgrrhlarfjmammsjivrkbnlyalihikphqjyywyrbjdewqwhytykuowvqjfxtppahaahwzyzkcdgscqsvocseapxmuwfllisniajjajucocwqsoojtgnvvmhrjpcwxwkhyvrzgnbvpaniqbtjjihevqxefbaeymoyihxoubljbztrcodmxmsscqwktyqrnesvlplhsxtvyopadumaghskxquqqnkdreafvmmolhjjwylzuazahtlgjhybukfoohvktjygrjpnkbmednhkgsqrbosyzzopjjzcszjllaaxdobgbkqjeiagzvgawupfdrkxqvjdvlabaehboaltknbjihjhbbmgswdkroopaoqauzdjboeoehxoojvpmkvegaoaperrvjrpkwamlgcrnzfbkbswlpctstvjxmauxtkipmwctytizzmkcgipwnkqgizfwzausmcjaymvwheviqhkwsbufoknwlssksmegqohqccojgmsytexnirswehspamcubibryiiamwmvketekqtskooqvihvvjswutpsdztryfmilgmvyiokwcarnkpivhgpcvihvdytklbvrqsrygcwlenyqeimlodpjnweqvzagbxztqsrywnlbcjthtfuhjktwgxpdzrjarkvjdmhzbtcfewmydjhmtalbacfztqbmbwvgkdhlykseghejqmylmlmmptnkkoxnmstwxajvmccujggbsgmhtaviujsgzptmiokfqudfyfzjnfkgnwpgwkosvjyvytjihtqaptfnaewnmivzekgdxwxsfwnepyozsebhzgxzmtnackaivinselmmjcsyagzslackgzmvubvylxhifwcmhpyqrqrrwsmjtqwbriwljukurtdzrhlzwjrpbkjzdvjwnfzenyrysdslwxkofvpdgitjtcjwzsumztsotjmlpexnejdlfsondjxwlgumaoabjspdebqvhpilzmygenvjysfkazycpzdbtsgztwubmdonpnvvcqfajmmlolodmrgfmmhfjbixgxmxkhtmxamiobucmkiydofpdmvoqdnwczumipyfpnqfokicwsczihplwmzmrmiunegvthdkwtqmfaobsqcczroxfpjxeuttybpskucgnussuivoaxrarhzwwlvcfqwfslxcfcluydotmljmiaobhoagzxigoelirlmypxsndiiptsdcuufekfkldurtbcbupntennsqwchrukvrgbvqghbldseexhzovutijnahphzmrudyvyqefspimwpldqaaktkvikdxrcjlymlwkbartrcinrttjttvoeqwovuixftyseuehuydnaldtewcarxovplmlhukmpietclayjfmjqpexnixehlcwyojfkuszeyuhlwfuctfuijrvtocacexauiigcafhabqmzxidroybzpxtgztifskzbsffumovpejoeruvhswhjvcpwxzbskcvcjazvrwmxhdbyxwirvraqtsnqrqidtdieghaxfowmrykowufrlikeazxtphzknhpvqruvfqhxotnlovczdogfnfadozpbggwwxstfjaexutkiopjtdrarwbwlalojunhtfbyobeoxyyhmnririikfjgsmtgvntehbfhpjmdgmeoyrhikpruwcaqqwxnjssstzcliqqrcufcoolydcvcgxsxtrkfkexfezqmrjdtdkwryhselnitmaqgsdlehkjnkccblhxqutksacynrggdjxldcwhlhsbtwdwhktyemizomzbfikkrjwuludydxzwucvbpobtdlutzuvgcfrvqprblubptblnfgruxuqagmvhgqokxhhnyyqjuuyovmbcsuxrpptxbpekhuwhdewbcplzjjpevsiqnfjcwdzaufkbcgifkfjpuuqfffjdxrvmzeoxjpxdxhfzqpgcwptqljvrqgwoarabvrahiykfhpgxhpcdevwshtlxchlcyofvffcnfpvngbmnsqrzmnrtgcqkjemjstezzjmgyjtgniufynemavfizytichtubavcjhijtepgollmyqzangjneexgnrcqrxuchfncjcizqtlolmpbtaozenitemkxmebvjoxutftjyhxmtmnoodqsqyoxkywycytomqifvcowjokeaxvpaljsjxpvxoucmpqygaebcuznijulipckandlnugkicousevafbdjvdzgottxivhikmtxjbkrgyoyfjykmbvhgupvniuxfdfqqapzczsiagifrirdlmnsjepwnjwsmbkeeadizysbgagaixftmsnvxctmlpeatrexrkfsixuqzaqhawcmqshpuabiqiijzmisynkikezjhrshpwvgocxleztujbfkpncocmwotxzaptjeqemgikrmlkjulqedggriupxpnwrcqaiigxoqhidssoogeujmcavwrumesdiigrsoojfxrirlyhrebardcmbugnaytjjzcdnsmupfeircpihslavpmwlummuhxfgzjvtxskdwsuzjeibriyhwwusiimpfsxgdvzcnjflbbkmgunxengakbssjhkrbjxeexitgofkrrwxomxszfvjgnesuqjxzgbgdkzmagwraurogqiivdterxwnphlpnovtawhcffufznviddqyhjcajanyhapxpksrjzuoeqvfdqngvfgcpjeajuatusqlckdnjzdppyuuqiamngqervgdpjwlboxfyctjdwysxuopcobswuyqrhtgqrtrhswhurqzqqtpkhepvgjuchktofbgyuxfnwmjpejhuewgmbxjjgdlqpgguhnsdmzsklccrnjnriufjrpuashsknyeunzzcysokwsdjercmlixezrgtyydnzijohisfajrwdxhhomvzwsfvlmolmsylchclqwssfkpjjyqxkmyigdfsrudeoerqlvbdstwxfnionbnanlivpopiktmazgqkbtqtootwbbmqcaqrlzncpclbxzbwhtjlmbecpzysbnidnzxaamdrqqsorvmboxmcasepsfjtssyhtxhvjmoaegqydezrcntcfzuxedsyxrfsoppaddailqioujfywadbazzgethekowbdmdjrdtdvbrrkzsgzvhbwiiacreofdrlruuiznluofmyeggfdphzyrbciisplkaceukehyaxdovjudoxtxwtqavyinqtzqxglhksfmqkbntvtkvmhtfytcybrowrhtzsdjmixevysowlarzikgigkihbzgugztacemncriclyywzrxjcdtkndrqczlkzgkdnxqpqatbzuzalwlpzezohtemsrytylxlkpcaqxbrrardycsxiunrnrffjebjpywznabdxcwpenucrobbiotvhadseebvezwrzxxzztqfjkhcykgjabgibjagpedvdanfxmexhuesemxeydnzeuhffjnxntstthyqvcpdwuxciuigxyfdsolzyayntrgmaefwiubeqyiytrhspmwjdjkdjjqdcxrcdwamrbshabivupnldlwguglercjvbaaexasoclxeofzkumxyytgubsyvwhqxiqdhtwvvjszzaalumiumbdjevhzrrsqbktidrfaczbdzbowqwsezvngsxflozbrkxbpqgqvhryhtnfjlzplvdrpaybqyejkbkzusrpzjnieapnmpczkhqzhqczqhiciscckvrmehuijkxvzcwljomtfpsvwbygtclgxeselomvamsbormxfbqksliqmiwhmjplojpbyeyyqtcekqdprwcjhmzvuycihstxbjbbnbcduejgumwmkaxrmzmgzroijhgmsjohksmhwvnqkleulemxdafcrtkcdsrxdffqzrxvnmnzyutjyhhdimhbitenovkrcrjbjgyyvnxthsehalkkatlknrxdmjwqbgtmmtkhhjcobhwduinuczgrqdufpqxqwtclmoutzzkcgigaqtxuudlnjhsyarqykulxkgsjfclnmtpdnozjslwduqduitvupgrzmmitqvidpyiemhngumlpcolmjghynaxbmfxfdfisfsyuzncuzojccwqmdxkqyitmpqrsybmftkzvycpzqaduwugbttttbngsfznddzjymktmmklekpzjlfkeyeybtgwyhjcmknlwxgkmryqdppmavxevdezwmvuueygqntplazxtxnwmfjocivxlzyhotdizeqqrkfcmgbferbswkhysexffwotrsbrwuhneossuvxamavklekfiknnibhztkqrezfipzckuzmjahvnliuvshjclsbecuyhtdrleuvatjjvrhkepfajollzdmgfgemcjeppampvvzrmibtxivgxgtyjfeookdsvjhkjtaeobvdjzyghtogzhfiolyewbyrkfcvaearfxwowuwgnmmovrwldwszyqskwwgyaiphflxehvkwjwkeqistfkufaorylxxnhovncutjqdgzbsgrbamimgnmxeniemxlauaepvqhyyicqottqibcqqrnxevdqvqsprzgopnnnwrdmmxfuahlryyoewtwrjricqprfcguaxzpjwuezbpqcpgglzdckunnkcereklhhkwsjqwirnavficqjfvtziglkkeqwrzfdvymnwwhmycrgejrjelkorxaebtcssiwoikdejksjnjsrtjdzupooposqhulcejqmvvteglotximsrrrmjhaywuofobhvkzjivcobqewpmkheeyqngslemblcftxruhzrloudsqsfdzljabwivjmhmzjrsjlpqkgdabhvtbcwdnhdqdllozsdydwtmhkcuqiurrrnstlvitaywnlnodqphmitusyqkimezerrzcpivpiufuhtzziilsehmexxmkblquepwtzslkosgvlfwwohqurdyqckcfxszbkvxlpkvdebarjwnzgetzjtpldsscmrfymekeqhhulkmuizvqfopqhhbmztqnmvmbawfqfonqyzkjafzgvpwewasxvimigyjiwqacensfmfonmnvketoctjbrtozzokhlakpgxjlkqzzdpupvnfyjobaipbjelrrnbgtarfmiglnxhcvvhvgywggojpuuiljltcmmjyusmjrtlmqvhwteebsnsojbzsouxaggbdanmsiaezxmxsqetkrnydozvfvshdbigbxvtgxyhumgmekhoeuohlpeqkxxpaiybftxnqvwmhfynphdvbrcmijeuicjikhjrcghsddgmigzancvrvaddjkxrmhzyqkpttwnyculmcmoqrkhmmmsxwrokapirbakwyxvctipwudolpxablsakjoukffdjfnfdmcgikxghcuusruveowoamjmuopfvekaspgazfgiiadctzzyovmqkxcgnrlixxjpmrqmxwuhzzjuzisnghfsghyuajcxgnmtfeheddlcdwycetrmcweidecfnhcwuqrzvydydqcgmcitvbfxxmgcqkherlcmctlztrzwhddufnndpuaogitxtadkofysykttdspmxugeivhzskpyuivplyazfyrfkmypgocdkkjsittafjyzrwpcwrdcrwjeiitoyxtikddsywudhscbqtfnmjrefakqkfeidatndwhbubgevkfmekbqvuwdwgthozrrzmgekphhsnlnysbecewayvdxdwervxkxkqbuhldzyonygqelvblvwqsbmytjydgiwkedvifvyuwhkashdfdzvvdjwwsuzbexlibisgdtczamauudbzfwuihsgzmfcqdnbgvvoboqcqeckailzpjwzqofsbmutriuzfqpighlxmphoxvooempvaupdjjxcttebltjsburpkadjvtaafpxgmmjxxizrcdsnzbhayyrizutuotwvjvbxhnufxtyzzqparwapvtzwntqdopbzkcwurqbpmzqnpfniepabibxxundleekpihlczmrnljacrnkvemwootmkipvpviedrpfqbyeokgqbwcyapwpdpdnzuloptuuklccmagcmpuplxnlojctafiabtqqolnywpdlrlpeaktljhzxsbqtjyvkuldiyqjxfmkwxzaalwlufmrxqhqzillczokzetwjhiihikhtguolhhjzpbyzpjbqynpejoqqwazekgatdqgmxrlotlnkuoaucrbnftdctdidlkwqadeaupopcezzsbvwtwjyppciunohxmyarcaouodwsfvngtlbpxahoerirfppspplurzoffmakkpsdcwszybnctxuapluecgytfoakbawlrrqunktlmjnfijhxwceyicrprsauuyhmrxgehbrvmhcvskupmynudfjwzlqtmxhdwnkfrbbdidabnvqzvftymfulqmhcloihesnvtqaetbhhyxitecurjoezdleocmwielfzbfdwikfgjocoswhbmlcpzigduelapqcsxfqgswodkqtcoafdohunqasmedpvvrpsygyqenuqfnswqzzeitrawjnaoewjvndtvemztipyvjwlivrrrkrnvgnjmluhbadwerwxzlxwxukfrbyimsxjanvnapwbpbyvsusthsqemcmffmoteldhayubnscfuaamwvignymbcaghnwbtkeakcwlrpqyjqbxpwfxlfjojmurztssdyvpatbtirstjttarazeijsrvokwhcqmancchfwrwqnhlgkeijiquckrqunazgmztoeatcurshbfnljxurqrtailuylteavxqbamdudxdgcsrlpoeffzfpkcnyxraurqvrcanixqoziimzwqfdrkscoicmzcisselxeyfeqvfadsabkfgcrbgijkwioedgiofppmtfiainsipfpvjiwrqhbmsptvxbjdsyrngzooniwennzwvynofqczfvufzektcbhibxyqfwutjvrhvhxdzzcfxxmwdwphxyqavqqbnmwwipfdwcgyelfbirzlnosmnknidflqshoaxufvyotezyfjpewevqridgsglewdnmfkilihbblactltxhyuzrecxxkkdiosvvddinmjoylstwmsfmnhdrjcqwmvecozyrfgersurdnkcbdjnqqqjcuaygveljejclricjdwpsgrtlaibtalvunvciznufwwqqfvzkroezhzlkhodhbabovdzwtteppufwrhikxmkhlvrujwblwebtkardtvulscjjlsuieepsbimkeqxcwzvgznlvigiakrmvlifsovkpfybkobmlcktbzfyhnikzayungzfwwpleqooercrtolxnsvxfejgghatpbblasyeimunewexnpuajszoyiwgpwbeacpavnedcysiwxfjocmywlouulaljdqjghjbxpgznzhmyoxoslmoxdktqmebqwlwewzbohcbglpgznvuyjixmvsehzgzvtxbrwefgijmtytvnopmxxlmuescdybatbelxkqftzsmanhndwbcwnqstjuyjyafzeqypiekkywkngxsebwconvjyrhjrhosogtfpzpbznlotkgalccbpzmpttzkdnftuaylznmaazowjuwxwaaocnfviehnumgqmgbntpnwobszvqyuqzksoppywxoqjwgydjlyybuoconaemwxnipdzhbvernpotnrebpecmsgagifsechotkoaljgdxwtslkzmbdqpwxqchxwmbdawpozaaffzbatnmsbqwsfsrxwyuumxxpumfvohawgewatlsubqogkhegiaauazlunrreytahxyhsjbpmudtenzlvbnrbndxawoewigdhhmasqpfkuaojzbecpyeedbebslxctdjarjvhaatvciedllfalleoplphyojrrsulersetmbvwiyhvfkgrqwgdlnbzyvtsreyiydbmgwiqwslbctsupyycnzcnwxgndgvbjwosuykqswswrkrhlpjaqnonmwapcytoujipjshcqzyimrpxgazzqnoclquqonelyochgjjxlkhxbywkyvlolztypnoecuraithretqpdxmgvkqtgbktcfrssiywepynkfgoaweftsmodejlivekaxeuhcqmtqbfwjuyfaeassoxwzigvorxovsvakjvbmbzvxzcxfcrxspwsxcpovocrgzttlqwxrxvoyxnecfbuuzotcfhxulqcnlxycvxvsukruzxweysayjwcofbitsngfkehgddayptsoqqvrixrtvvibwsuqfawsgfalkcjzwdqovnhgkyzivhjscfijfgdnodyygkaepsulfcrrcszycisepapwjtjxwkxewxklpfywjronkploadspghmrcxqbhnffnstezrbklrxxgjlgofywmknrhdsrtxygrrmqlnawgyvnjgvzltwzflqpriikigszaesluujauepdknfxibwoonffxnpftjhtqbgkvpmqtcvfpacxdznsosxnfptbycwoddayunqormvimyhqzvknphcxwvaxzwncbodybtouhjcuhlmgiyvyfyxevxdvvqzzeexhalbhufderrkzpizxiwbdtgapwcqbinkiamswtvaknnmevlbfieidklshnkkxxuiziawcxwomlariosnwzwzjjuqyecvexddhfbldaaplciuqdhocfolqkeoogmufpanvbaabarpfajxdsmfacsqmyhcftxmizbfcchgezvjzgjeavlaxdtlcanjtmvdlzlobsuhrrtsxcwxxhawnthrtucojzruyckzvgjmxcfwedudnuzanitievwnunkvsuwndfbahixlotobppdcxwmcrkpnzzirwfgbkibssafgvuhkjkohialbkapkczdagkbtuenmhsvcoenarbjzeubqwsaateacqdvkikyrcvttaivrmesqavgwpjxjpznhfirpsrgwnbrnkmgyqaqswypnhoyyplfuvylpqrodtfsfsadkatfyrwmbkmbbyhythjlxdzcwewdywglzbqzumnvyaxbagzvplgpofrmkqpkovvpynpsbeozgnbgvcckpkzdqtpcjemxbknzzesbiicpxdxsizexkgdczuekbsjceyeecyfnghcdnbxxbbwnjzriwxuxpezucfafdfslowqdxnaarxpayilwfftvjvrmartgynroliskvunotersncqsjkptfihhbcnzpfqcnimkczzwesqrugldsbyxjfhnjuoyzecoopzroapuuhnopzticshnzoajjpjkvmzkdabtcsowzdmqehygzgwbuwmfnxsjlrtotwixoyvpbjfgqgosmkvijhqwgifsbaiwwstmqqduzlcrrqjfdepmnfkwnsoqsymrrhfhxjdyufqlybsdihpxnbtctjtoihhzpmgovmprrheriwuselqtplxkvsydafcrukhpwwjqdnjomeiqrylgmkrhdrkfzowtydkxatnfjyvvcelweyeqixxlpjsqxojyuvxwpmbykztpdgljgraopzcgjuwilhifcfbtretedmtiuesaxsrmtvuerspcbxjgfmzytvcyjvhebzgztznouktmciqghcmoqlnjgpiqnpwqqerlefbypumtefzmjlazzpjhhtzukxmacengjogalvvpcxdlkemjvvtcouyyulawppeagmcrhxglwmwhsjqnglqxioxcbayspesvqwoawxlsjkzbtqobdgylxynyyntntllkkzkgyxyhhykcqbethehgcwhcmaqfndpxebddbcmiaxnqytlhxuocrvedxwkkzcigfnjgpxprwcjuvveuruyirfnobaadcilhwwontffqhomelsadmzndgdtjduofezmavcqphvhqlvwzoxeayrgewznztcgadtazxsqfpzvbuucirgjrzpxwqkxmoemuzotwhlbwkzzevbnmjydjpchfoetdkfzjwsgdfjbpkbvfektoiyzzaihpoauzitienqjsckjongwurpibqjbqrihhkbgswryljhflsoahxwbonlrduuwncdxphdhfwgrgnwthntrkrsahermamiqqonfxspcpxtxmqqudmnpdfpmlizoujgnzvuwnjzegsbtkspngccljtyxcznyitlkqggfrfmyantkhianmcbxwzwayjyiekuusbajiojibctlmtaaxbyvcuvcgunkghhaijjrxtbavulkpoknrkkuhiynelzktgkdpvwmoynmuaykqizivlectcpxqojlxvomrnbhnothqtthcupxgvbzxszniiyfgpuxeverlaabtuixozwwuxyurxjahkfnzbmfwtwhvwjostohtmfpmdjdctdkdlzemmjlfhsadbqwvgfqtkffqpkskqepbevpseazlvbqwtotatlvgrcyioquexjhbgxvkzuxuxptqeoszaphttfbiwxmtiuwottaspzpmoieuwxuyobrihuqfrcazyynrrpkgozudjyxhvtgkxzueuklnolpnjeecuoiipclaaliygqkdpehlqsbefqrquwsqmazeemehzofgerjwxtjnnkrtcjjzhcpteoxjdeqcsxixosvlleyyrrttcdsjhkdlacwdgmizlqwzktmxxmyogriiwcsdovrpznugccfntdpfwddvqbkwsuerywuntnetdybfbguwljbjngefhqdakhtlgpybdcwgcxnffhdsthbininvyqxlzqwhfwjiahqcffkmnnfguioiqddrvaeusaexypiywacdgmqtavbufrewwhprjtnbvrbtgjrfltirgamixnedgjbcsqvejjfeaizjtqoflywtzjbwyizhrallshpbqvhsfgdzytgkseftnjporrvktgvmplpfizanhdogxusrzzkoibebublokhczsthcshramgilccedbosmsynmazckiejcyseqzvsodczgeejiudwmcjbekdqsibuiuyavwtjzxlherrolwkaatdeeguwqytystznpuxrtkyxbrloqvqqptxvatrqrmrjgsxvmwofinfjgqxwmondhmyjfrcxetiklfhzdwglllwrcwqqkfttrtfwkhvoceanliorguctgbmixcyhhtcamhxwqsnsyphkxvbfqfywglgdpgmxzpxlywjprwjpmrzlmcteiraoeisuogtnvsawpkniiwxunzicdbglsjczrwtgcmvyewwvgjdofdlvetxhwdvqmxpgtimvwjvdftancgcijpdpicygftwusmalwojtxgyfaysceumplrettfbbyyvrkxegnpbkybpyaicgerwqiclchnfinabxzffmxjwvkovmyzteqrwbtifdxknkmojlvqxsztnmjkyhktmckifgsklrwydiootjfqcgmrsxetfqmtszdyfyksrhqvrellpqdtxrnrprkwhzpzyuzfsmxktphmvszmldgkwtbnkojrpaspvuupgtbbkknffptquzaqsdeetpxiqqxnmteuogvyskfxzzntypmtvqxohvzxnymbsrvgzqhtcmrengxmyjhtbejlbiiqhxrbqmjreqkhfdlskkgiwndzumkvvvmesffksqbwhldopqgbbplxcowyahwxcibwpighbheiujylagobvzaapwyqfupjetfudnbewhorrmetttuqsuqksraanrjskroqgrudbjwsvalqvhhodzyxqaxetjygaowgfqlgzhaxinpduytzytxqvuwrdwxfktoslzanhbkrqbwlaqmaljqjgpallxtyshqdgqqptcgkedxevjgivyrdnrobojzgqrmzjcqffxrlcorzzxhwvbzjsqmjznrsgdrpghwngnykdpldmtzjwbsorgzqtrizubrclpprdpegeplskncgowxfdwxyniykjrmugeoltssahfsusuagrznwwlultuvclkzuonfjfxjofcixylermrnieiuxcrcqbbkropbtpkjuournhxetrsevcatervwvwgmmynfnyqjokabtagnratocthikefhcnuolhvahmjwymzsmhhfhatlvdwhhdpkqjaesweakoyicxcofltonociryqzbhltqlzijektuieyiimpuhdjxhspfkqirbejodrajcvfmzdwkrlgarpyyjnetdowoikdejksjnjsrtjdzupooposqhulcejqmvvteglotximsrrrmjhaywuofobhvkzjivcobqewpmkheeyqngslemblcftxruhzrloudsqsfdzljabwivjmhmzjrsjlpqkgdabhvtbcwdnhdqdllozsdydwtmhkcuqiurrrnstlvitaywnlnodqphmitusyqkimezerrzcpivpiufuhtzziilsehmexxmkblquepwtzslkosgvlfwwohqurdyqckcfxszbkvxlpkvdebarjwnzgetzjtpldsscmrfymekeqhhulkmuizvqfopqhhbmztqnmvmbawfqfonqyzkjafzgvpwewasxvimigyjiwqacensfmfonmnvketoctjbrtozzokhlakpgxjlkqzzdpupvnfyjobaipbjelrrnbgtarfmiglnxhcvvhvgywggojpuuiljltcmmjyusmjrtlmqvhwteebsnsojbzsouxaggbdanmsiaezxmxsqetkrnydozvfvshdbigbxvtgxyhumgmekhoeuohlpeqkxxpaiybftxnqvwmhfynphdvbrcmijeuicjikhjrcghsddgmigzancvrvaddjkxrmhzyqkpttwnyculmcmoqrkhmmmsxwrokapirbakwyxvctipwudolpxablsakjoukffdjfnfdmcgikxghcuusruveowoamjmuopfvekaspgazfgiiadctzzyovmqkxcgnrlixxjpmrqmxwuhzzjuzisnghfsghyuajcxgnmtfeheddlcdwycetrmcweidecfnhcwuqrzvydydqcgmcitvbfxxmgcqkherlcmctlztrzwhddufnndpuaogitxtadkofysykttdspmxugeivhzskpyuivplyazfyrfkmypgocdkkjsittafjyzrwpcwrdcrwjeiitoyxtikddsywudhscbqtfnmjrefakqkfeidatndwhbubgevkfmekbqvuwdwgthozrrzmgekphhsnlnysbecewayvdxdwervxkxkqbuhldzyonygqelvblvwqsbmytjydgiwkedvifvyuwhkashdfdzvvdjwwsuzbexlibisgdtczamauudbzfwuihsgzmfcqdnbgvvoboqcqeckailzpjwzqofsbmutriuzfqpighlxmphoxvooempvaupdjjxcttebltjsburpkadjvtaafpxgmmjxxizrcdsnzbhayyrizutuotwvjvbxhnufxtyzzqparwapvtzwntqdopbzkcwurqbpmzqnpfniepabibxxundleekpihlczmrnljacrnkvemwootmkipvpviedrpfqbyeokgqbwcyapwpdpdnzuloptuuklccmagcmpuplxnlojctafiabtqqolnywpdlrlpeaktljhzxsbqtjyvkuldiyqjxfmkwxzaalwlufmrxqhqzillczokzetwjhiihikhtguolhhjzpbyzpjbqynpejoqqwazekgatdqgmxrlotlnkuoaucrbnftdctdidlkwqadeaupopcezzsbvwtwjyppciunohxmyarcaouodwsfvngtlbpxahoerirfppspplurzoffmakkpsdcwszybnctxuapluecgytfoakbawlrrqunktlmjnfijhxwceyicrprsauuyhmrxgehbrvmhcvskupmynudfjwzlqtmxhdwnkfrbbdidabnvqzvftymfulqmhcloihesnvtqaetbhhyxitecurjoezdleocmwielfzbfdwikfgjocoswhbmlcpzigduelapqcsxfqgswodkqtcoafdohunqasmedpvvrpsygyqenuqfnswqzzeitrawjnaoewjvndtvemztipyvjwlivrrrkrnvgnjmluhbadwerwxzlxwxukfrbyimsxjanvnapwbpbyvsusthsqemcmffmoteldhayubnscfuaamwvignymbcaghnwbtkeakcwlrpqyjqbxpwfxlfjojmurztssdyvpatbtirstjttarazeijsrvokwhcqmancchfwrwqnhlgkeijiquckrqunazgmztoeatcurshbfnljxurqrtailuylteavxqbamdudxdgcsrlpoeffzfpkcnyxraurqvrcanixqoziimzwqfdrkscoicmzcisselxeyfeqvfadsabkfgcrbgijkwioedgiofppmtfiainsipfpvjiwrqhbmsptvxbjdsyrngzooniwennzwvynofqczfvufzektcbhibxyqfwutjvrhvhxdzzcfxxmwdwphxyqavqqbnmwwipfdwcgyelfbirzlnosmnknidflqshoaxufvyotezyfjpewevqridgsglewdnmfkilihbblactltxhyuzrecxxkkdiosvvddinmjoylstwmsfmnhdrjcqwmvecozyrfgersurdnkcbdjnqqqjcuaygveljejclricjdwpsgrtlaibtalvunvciznufwwqqfvzkroezhzlkhodhbabovdzwtteppufwrhikxmkhlvrujwblwebtkardtvulscjjlsuieepsbimkeqxcwzvgznlvigiakrmvlifsovkpfybkobmlcktbzfyhnikzayungzfwwpleqooercrtolxnsvxfejgghatpbblasyeimunewexnpuajszoyiwgpwbeacpavnedcysiwxfjocmywlouulaljdqjghjbxpgznzhmyoxoslmoxdktqmebqwlwewzbohcbglpgznvuyjixmvsehzgzvtxbrwefgijmtytvnopmxxlmuescdybatbelxkqftzsmanhndwbcwnqstjuyjyafzeqypiekkywkngxsebwconvjyrhjrhosogtfpzpbznlotkgalccbpzmpttzkdnftuaylznmaazowjuwxwaaocnfviehnumgqmgbntpnwobszvqyuqzksoppywxoqjwgydjlyybuoconaemwxnipdzhbvernpotnrebpecmsgagifsechotkoaljgdxwtslkzmbdqpwxqchxwmbdawpozaaffzbatnmsbqwsfsrxwyuumxxpumfvohawgewatlsubqogkhegiaauazlunrreytahxyhsjbpmudtenzlvbnrbndxawoewigdhhmasqpfkuaojzbecpyeedbebslxctdjarjvhaatvciedllfalleoplphyojrrsulersetmbvwiyhvfkgrqwgdlnbzyvtsreyiydbmgwiqwslbctsupyycnzcnwxgndgvbjwosuykqswswrkrhlpjaqnonmwapcytoujipjshcqzyimrpxgazzqnoclquqonelyochgjjxlkhxbywkyvlolztypnoecuraithretqpdxmgvkqtgbktcfrssiywepynkfgoaweftsmodejlivekaxeuhcqmtqbfwjuyfaeassoxwzigvorxovsvakjvbmbzvxzcxfcrxspwsxcpovocrgzttlqwxrxvoyxnecfbuuzotcfhxulqcnlxycvxvsukruzxweysayjwcofbitsngfkehgddayptsoqqvrixrtvvibwsuqfawsgfalkcjzwdqovnhgkyzivhjscfijfgdnodyygkaepsulfcrrcszycisepapwjtjxwkxewxklpfywjronkploadspghmrcxqbhnffnstezrbklrxxgjlgofywmknrhdsrtxygrrmqlnawgyvnjgvzltwzflqpriikigszaesluujauepdknfxibwoonffxnpftjhtqbgkvpmqtcvfpacxdznsosxnfptbycwoddayunqormvimyhqzvknphcxwvaxzwncbodybtouhjcuhlmgiyvyfyxevxdvvqzzeexhalbhufderrkzpizxiwbdtgapwcqbinkiamswtvaknnmevlbfieidklshnkkxxuiziawcxwomlariosnwzwzjjuqyecvexddhfbldaaplciuqdhocfolqkeoogmufpanvbaabarpfajxdsmfacsqmyhcftxmizbfcchgezvjzgjeavlaxdtlcanjtmvdlzlobsuhrrtsxcwxxhawnthrtucojzruyckzvgjmxcfwedudnuzanitievwnunkvsuwndfbahixlotobppdcxwmcrkpnzzirwfgbkibssafgvuhkjkohialbkapkczdagkbtuenmhsvcoenarbjzeubqwsaateacqdvkikyrcvttaivrmesqavgwpjxjpznhfirpsrgwnbrnkmgyqaqswypnhoyyplfuvylpqrodtfsfsadkatfyrwmbkmbbyhythjlxdzcwewdywglzbqzumnvyaxbagzvplgpofrmkqpkovvpynpsbeozgnbgvcckpkzdqtpcjemxbknzzesbiicpxdxsizexkgdczuekbsjceyeecyfnghcdnbxxbbwnjzriwxuxpezucfafdfslowqdxnaarxpayilwfftvjvrmartgynroliskvunotersncqsjkptfihhbcnzpfqcnimkczzwesqrugldsbyxjfhnjuoyzecoopzroapuuhnopzticshnzoajjpjkvmzkdabtcsowzdmqehygzgwbuwmfnxsjlrtotwixoyvpbjfgqgosmkvijhqwgifsbaiwwstmqqduzlcrrqjfdepmnfkwnsoqsymrrhfhxjdyufqlybsdihpxnbtctjtoihhzpmgovmprrheriwuselqtplxkvsydafcrukhpwwjqdnjomeiqrylgmkrhdrkfzowtydkxatnfjyvvcelweyeqixxlpjsqxojyuvxwpmbykztpdgljgraopzcgjuwilhifcfbtretedmtiuesaxsrmtvuerspcbxjgfmzytvcyjvhebzgztznouktmciqghcmoqlnjgpiqnpwqqerlefbypumtefzmjlazzpjhhtzukxmacengjogalvvpcxdlkemjvvtcouyyulawppeagmcrhxglwmwhsjqnglqxioxcbayspesvqwoawxlsjkzbtqobdgylxynyyntntllkkzkgyxyhhykcqbethehgcwhcmaqfndpxebddbcmiaxnqytlhxuocrvedxwkkzcigfnjgpxprwcjuvveuruyirfnobaadcilhwwontffqhomelsadmzndgdtjduofezmavcqphvhqlvwzoxeayrgewznztcgadtazxsqfpzvbuucirgjrzpxwqkxmoemuzotwhlbwkzzevbnmjydjpchfoetdkfzjwsgdfjbpkbvfektoiyzzaihpoauzitienqjsckjongwurpibqjbqrihhkbgswryljhflsoahxwbonlrduuwncdxphdhfwgrgnwthntrkrsahermamiqqonfxspcpxtxmqqudmnpdfpmlizoujgnzvuwnjzegsbtkspngccljtyxcznyitlkqggfrfmyantkhianmcbxwzwayjyiekuusbajiojibctlmtaaxbyvcuvcgunkghhaijjrxtbavulkpoknrkkuhiynelzktgkdpvwmoynmuaykqizivlectcpxqojlxvomrnbhnothqtthcupxgvbzxszniiyfgpuxeverlaabtuixozwwuxyurxjahkfnzbmfwtwhvwjostohtmfpmdjdctdkdlzemmjlfhsadbqwvgfqtkffqpkskqepbevpseazlvbqwtotatlvgrcyioquexjhbgxvkzuxuxptqeoszaphttfbiwxmtiuwottaspzpmoieuwxuyobrihuqfrcazyynrrpkgozudjyxhvtgkxzueuklnolpnjeecuoiipclaaliygqkdpehlqsbefqrquwsqmazeemehzofgerjwxtjnnkrtcjjzhcpteoxjdeqcsxixosvlleyyrrttcdsjhkdlacwdgmizlqwzktmxxmyogriiwcsdovrpznugccfntdpfwddvqbkwsuerywuntnetdybfbguwljbjngefhqdakhtlgpybdcwgcxnffhdsthbininvyqxlzqwhfwjiahqcffkmnnfguioiqddrvaeusaexypiywacdgmqtavbufrewwhprjtnbvrbtgjrfltirgamixnedgjbcsqvejjfeaizjtqoflywtzjbwyizhrallshpbqvhsfgdzytgkseftnjporrvktgvmplpfizanhdogxusrzzkoibebublokhczsthcshramgilccedbosmsynmazckiejcyseqzvsodczgeejiudwmcjbekdqsibuiuyavwtjzxlherrolwkaatdeeguwqytystznpuxrtkyxbrloqvqqptxvatrqrmrjgsxvmwofinfjgqxwmondhmyjfrcxetiklfhzdwglllwrcwqqkfttrtfwkhvoceanliorguctgbmixcyhhtcamhxwqsnsyphkxvbfqfywglgdpgmxzpxlywjprwjpmrzlmcteiraoeisuogtnvsawpkniiwxunzicdbglsjczrwtgcmvyewwvgjdofdlvetxhwdvqmxpgtimvwjvdftancgcijpdpicygftwusmalwojtxgyfaysceumplrettfbbyyvrkxegnpbkybpyaicgerwqiclchnfinabxzffmxjwvkovmyzteqrwbtifdxknkmojlvqxsztnmjkyhktmckifgsklrwydiootjfqcgmrsxetfqmtszdyfyksrhqvrellpqdtxrnrprkwhzpzyuzfsmxktphmvszmldgkwtbnkojrpaspvuupgtbbkknffptquzaqsdeetpxiqqxnmteuogvyskfxzzntypmtvqxohvzxnymbsrvgzqhtcmrengxmyjhtbejlbiiqhxrbqmjreqkhfdlskkgiwndzumkvvvmesffksqbwhldopqgbbplxcowyahwxcibwpighbheiujylagobvzaapwyqfupjetfudnbewhorrmetttuqsuqksraanrjskroqgrudbjwsvalqvhhodzyxqaxetjygaowgfqlgzhaxinpduytzytxqvuwrdwxfktoslzanhbkrqbwlaqmaljqjgpallxtyshqdgqqptcgkedxevjgivyrdnrobojzgqrmzjcqffxrlcorzzxhwvbzjsqmjznrsgdrpghwngnykdpldmtzjwbsorgzqtrizubrclpprdpegeplskncgowxfdwxyniykjrmugeoltssahfsusuagrznwwlultuvclkzuonfjfxjofcixylermrnieiuxcrcqbbkropbtpkjuournhxetrsevcatervwvwgmmynfnyqjokabtagnratocthikefhcnuolhvahmjwymzsmhhfhatlvdwhhdpkqjaesweakoyicxcofltonociryqzbhltqlzijektuieyiimpuhdjxhspfkqirbejodrajcvfmzdwkrlgarpyyjnetdo"
sol = Solution()
print(sol.longestDupSubstring(s))
