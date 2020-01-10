def get_response(last_message, domain_name="http://localhost:8000/", language="english"):
    small_case_message = last_message.lower()

    if language == "english":
        if "start" in small_case_message:
            return '''
            Welcome To Kautilya! In order to access any of the given information. Send the number below: 
                1. Syllabus & Learning Resources
                2. Crowdsourcing
                3. Events Nearby (Map)
                4. Video Conference
                5. Analytics
                6. Donation
                7. भाषा को स्थानीय भाषा में बदलें
            ''', language

        if any([True for word in small_case_message.split(" ") if word in ["1", "syllabus"]]):
            return "Recommended Syllabus with all of the learning material can be found at: {}syllabus".format(domain_name),language

        if any([True for word in small_case_message.split(" ") if word in ["2", "crowdsourcing"]]):
            return "Crowdsourcing Platform with all of the necessary details can be found at: {}crowdsourcing".format(domain_name)

        if any([True for word in small_case_message.split(" ") if word in ["3", "map", "events"]]):
            return "Events happening nearby with a local map navigator can be found at: {}map".format(domain_name)

        if any([True for word in small_case_message.split(" ") if word in ["4", "video", "conference"]]):
            return "Video Conference Platform with all of the necessary details can be found at: {}conference".format(domain_name)

        if any([True for word in small_case_message.split(" ") if word in ["5", "analytics"]]):
            return "Analytics on various metrics about our mission can be found at: {}analytics".format(domain_name)

        if any([True for word in small_case_message.split(" ") if word in ["6", "donation"]]):
            return "Donating details can be found at: {}crowdsourcing".format(domain_name)
        # change below to hindi translate
        if any([True for word in small_case_message.split(" ") if word in ["7", "language"]]):
            return '''
            Kautilya में आपका स्वागत है! किसी भी जानकारी को एक्सेस करने के लिए। नीचे की संख्या भेजें:
                 1. सिलेबस और लर्निंग रिसोर्स
                 2. क्राउडसोर्सिंग
                 3. घटनाएँ (मानचित्र)
                 4. वीडियो कॉन्फ्रेंस
                 5. एनालिटिक्स
                 6. दान
                 7. Change language to English
            ''', "hindi"
    else:
        if "start" in small_case_message:
            return '''
            Kautilya में आपका स्वागत है! किसी भी जानकारी को एक्सेस करने के लिए। नीचे की संख्या भेजें:
                 1. सिलेबस और लर्निंग रिसोर्स
                 2. क्राउडसोर्सिंग
                 3. घटनाएँ (मानचित्र)
                 4. वीडियो कॉन्फ्रेंस
                 5. एनालिटिक्स
                 6. दान
                 7. Change language to English
            ''', language

        if any([True for word in small_case_message.split(" ") if word in ["1", "syllabus"]]):
            return "सभी सीखने की सामग्री के साथ अनुशंसित सिलेबस पाया जा सकता है: {}syllabus".format(domain_name),language

        if any([True for word in small_case_message.split(" ") if word in ["2", "crowdsourcing"]]):
            return "सभी आवश्यक विवरणों के साथ क्राउडसोर्सिंग प्लेटफार्म पर पाया जा सकता है: {}crowdsourcing".format(domain_name)

        if any([True for word in small_case_message.split(" ") if word in ["3", "map", "events"]]):
            return "स्थानीय मानचित्र नेविगेटर के साथ होने वाली घटनाओं पर पाया जा सकता है: {}map".format(domain_name)

        if any([True for word in small_case_message.split(" ") if word in ["4", "video", "conference"]]):
            return "सभी आवश्यक विवरणों के साथ वीडियो सम्मेलन मंच पर पाया जा सकता है: {}conference".format(domain_name)

        if any([True for word in small_case_message.split(" ") if word in ["5", "analytics"]]):
            return "हमारे मिशन के बारे में विभिन्न मैट्रिक्स पर विश्लेषण पाया जा सकता है: {}analytics".format(domain_name)

        if any([True for word in small_case_message.split(" ") if word in ["6", "donation"]]):
            return "दान विवरण में पाया जा सकता है: {}crowdsourcing".format(domain_name)
        
        if any([True for word in small_case_message.split(" ") if word in ["7", "language"]]):
            return '''
            Kautilya में आपका स्वागत है! किसी भी जानकारी को एक्सेस करने के लिए। नीचे की संख्या भेजें:
                 1. सिलेबस और लर्निंग रिसोर्स
                 2. क्राउडसोर्सिंग
                 3. घटनाएँ (मानचित्र)
                 4. वीडियो कॉन्फ्रेंस
                 5. एनालिटिक्स
                 6. दान
                 7. Change language to English
            ''', "english"

    return False
