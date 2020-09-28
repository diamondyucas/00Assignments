class Participant:
    def __init__(self, name, is_muted = True):
        self.name = name
        self.is_muted = is_muted       # Come into meetings muted
        self.profile_pic = ""       # Path to a user's image

    def change_name(self, new_name):
        if len(new_name) > 0:
            self.name = new_name

    def toggle_mute(self):
        self.is_muted = not self.is_muted


class Meeting:
    def __init__(self, host, topic, recur = False, pw = None, participants=[]):
        """
        Constructor of the Meeting class

        :param host: A Participant object representing the host of the meeting
        :param topic: A string representing the meeting's title/topic
        :param recur: A boolean representing if the meeting is one time (False) or recurring (True)
        :param pw: A string representing the password to join the meeting. Defaults to None if no password needed.
        """
        self.host = host
        self.topic = topic
        self.recurring = recur
        self.id = random.randint(0, 999999)
        self.password = pw      # None by default, since a password is not required
        self.participants = participants

        # ... obviously there's more attributes in the real Zoom application,
        #     but we won't be needing them for this assignment

    def start_meeting(self):
        """
        Kicks off the Zoom meeting

        :return: None
        """
        print("Starting the {} meeting".format(self.topic))

    def end_meeting(self):
        """
        Ends the meeting for all participants.

        :return: None
        """
        print("Ending the {} meeting. Bye!".format(self.topic))
        sleep(3)
        quit()

    def print_participants(self):
        """
        Prints an updated list of participants. Call it each time the participant's in the meeting change.

        :return: None
        """
        print("Your meeting now has {0} participants:".format(len(self.participants) + 1))      # +1 is the host
        print("{0} (Host): {1}".format(self.host, "Muted" if self.host.is_muted else "Unmuted"))
        for participant in self.participants:
            print("{0}: {1}".format(participant.name, "Muted" if self.host.is_muted else "Unmuted"))


    def add_participant(self, participant):
        """
        Adds participant to the list of participants
        """
        self.participants.append(participant)


    def remove_participant(self, participant):
        """
        Removes participant to the list of participants
        """
        self.participants.remove(participant)

