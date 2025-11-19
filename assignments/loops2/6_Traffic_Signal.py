"""
Problem:SmartTrafficSignalDecisionSystem.
    - YouaredesigninganAItrafficcontrollerforasmartintersection.
    - Yoursystemmustdecidewhethervehiclescanmoveormuststop, basedonseveralreal-worldconditions.
    - Eachdecisionmustbelogical,exclusive,andbasedonpriority—safetyfirst.

    Scenario:
    At a four-wayintersection,thetrafficlightsystemmustdecidewhat
    messagetodisplaytoapproachingvehiclesbasedonthese
    conditions(allareuserinputsas'yes'or'no').

    DecisionRules(instrictpriorityorder):
    1.EmergencyOverride:
    If there’ sanemergencyvehiclenearby,alltrafficmuststop,no
    matterwhat

    2. PedestrianSafety:
    Ifpedestriansarecrossing,vehiclesmuststop,evenifthelightis
    green.

    3.AccidentZone:
    If ana ccident is reported ahead,display
    "Caution:AccidentAhead.ProceedSlowly.

    4.HeavyRainCondition:
    If it’s sheavilyrainingandthelightisred,display"WaitforGreen
    VisibilityLow."
    Ifit’ sheavilyrainingandthelightisgreen,display"ProceedSlowly
    WetRoads."

    5.SchoolZonePriority:
    If it’ saschoolzoneandthetimeisrushhour,show"ExtraCaution:
    SchoolZoneduringRushHour."
    Otherwise,ifonlyschoolzoneisactive,show"DriveCarefully-School
    Zone.

    6.NormalCondition:
    Ifthelightisgreen,show"Youmaygo."
    Otherwise,show"Stopandwaitforgreen."
    Theprogramshouldprintexactlyonedecisionmessage,accordingto thefirstmatchingconditionintheaboveprioritylist


"""

emergency = input("Is there an emergency vehicle nearby? (yes/no): ")
pedestrians = input("Are pedestrians currently crossing? (yes/no): ")
green_signal = input("Is the traffic light green? (yes/no): ")
rain = input("Is it raining heavily? (yes/no): ")
accident = input("Is there an accident reported ahead? (yes/no): ")
school_zone = input("Is this a school zone? (yes/no): ")
rush_hour = input("Is it rush hour? (yes/no): ")

if emergency == "yes":
    print("All Traffic Stop: Emergency Vehicle Passing.")

elif pedestrians == "yes":
    print("Stop: Pedestrians Crossing.")

elif accident == "yes":
    print("Caution: Accident Ahead. Proceed Slowly.")

elif rain == "yes":
    if green_signal == "yes":
        print("Proceed Slowly - Wet Roads.")
    else:
        print("Wait for Green - Visibility Low.")

elif school_zone == "yes" and rush_hour == "yes":
    print("Extra Caution: School Zone during Rush Hour.")

elif school_zone == "yes":
    print("Drive Carefully - School Zone.")

elif green_signal == "yes":
    print("You may go.")

else:
    print("Stop and wait for green.")