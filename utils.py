def get_response(last_message, domain_name="http://localhost:8000/"):
    small_case_message = last_message.lower()

    if "start" in small_case_message:
        return '''
        Welcome To Kautilya! In order to access any of the given information. Send the number below: 
            1. Syllabus & Learning Resources
            2. Crowdsourcing
            3. Events Nearby (Map)
            4. Video Conference
            5. Analytics
            6. Donation
        '''

    if any([True for word in small_case_message.split(" ") if word in ["1", "syllabus"]]):
        return "Recommended Syllabus with all of the learning material can be found at: {}syllabus".format(domain_name)

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

    return False
