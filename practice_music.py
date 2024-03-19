#SMALL PROBLEMS TO TACKLE
# Create a random note generator
# Create a major chord of random note or requested note
# Create a minor chord of a random note or requested note
# Create common chord progressions to practice to
# Create a class for generating chords
# remove note practiced to a list till restart
# DOE - 01.19.24: Been thinking about creating a practice app for sometime now to help me with my practice
import random

class GenerateNote:
    """
    A class to help control all areas of generating notes, chords, and common
    chord progressions
    """

    def __init__(self):
        """
        Initializing data members 
        """

        self._all_mode_list = ['major', 'minor']
      
        self._mode = 'major'   #Choices - major or minor with major being default setting

        self._note = 'G'       # Choices will be from all list of notes with default being G

        self._all_notes = [['Ab', 'G#'], 'A', ['A#', 'Bb'], 'B', 'C', ['C#',\
                            'Db'], 'D', ['D#','Eb'], 'E', 'F', ['F#', \
                            'Gb'], 'G', 'G#']
        
        self._natural_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

        self._accidental_notes = [['Ab', 'G#'], ['A#', 'Bb'], ['C#', 'Db'],\
                                   ['D#', 'Eb'],['F#', 'Gb']]
        
    def get_mode(self):
        """
        Returns mode of music
        """

        return self._mode
    
    def set_mode(self, requested_mode):
        """sets mode to desired setting"""
        
        self._mode = requested_mode
    
    def get_note(self):
        """Returns note"""

        return self._note
    
    def set_note(self, requested_note):
        """Sets note to requested"""

        self._note = requested_note

    def get_mode_list(self):
        """
        Returns list of mode
        """

        return self._all_mode_list
    
    def generate_mode(self):
        """
        Generate random mode 
        """
        mode = random.choice(self.get_mode_list())
        self.set_mode(mode)

    def get_all_notes(self):
        """
        Returns list of all standard western notes
        """

        return self._all_notes
    
    def get_accidental_notes(self):
        """
        Returns list of all standard western accidental notes
        """

        return self._accidental_notes
    

    def get_natural_notes(self):
        """
        Returns list of all standard western accidental notes
        """

        return self._natural_notes
    
    
    def generate_all_notes(self, randomize_all, note, mode):
        """
        Generate random note from natural-Accidental list
        """

        random_note = random.choice(self.get_all_notes())
        
        # randomizes all aspect of generating a note
        if randomize_all == 'yes' or note == 'random' and mode == 'random':
            self.generate_mode()
            return random.choice(random_note) +' '+ self.get_mode()
        
        #randomizes note generation with requested mode of practice
        if note == 'random' and mode != 'random':
            self.set_mode(mode)
            return random.choice(random_note) +' '+ self._mode 
        
        #randomizes mode generation with requested note of practice
        if note != 'random' and mode == 'random':
            self.set_note(note)
            self.generate_mode()
            return self.get_note() +' '+ self.get_mode()

    def generate_natural_notes(self):
        """
        Generate random note from natural list
        """

        return random.choice(self.get_natural_notes()) +' '+ \
            self.generate_mode()
    
    def generate_accidental_notes(self):
        """
        Generate random note from natural list
        """

        random_list = random.choice(self.get_accidental_notes()) 
        
        # Return random note from list of 2 equivalent notes 
        # [Eb, D#] - randomly pick between the two
        return random.choice(random_list) +' '+ self.generate_mode()
    



def main():
    # mode = MusicPractice().generate_mode()
    # play_accidentals = GenerateNote().generate_accidental_notes()
    # play_accid_nat = GenerateNote().generate_all_notes()
    # play_natural = GenerateNote().generate_natural_notes()
    # print('Accidentals:',play_accidentals)
    # print('Mixed notes:',play_accid_nat)
    # print('Natural note:',play_natural)
    
    play = GenerateNote()
    notes = play.get_all_notes()
    modes = play.get_mode_list()

    #DIRECTIONS
    print("All notes you can choose to practice:")
    for note in notes:
        print(note)
    print("All modes you can choose to practice:")
    for mode in modes:
        print(mode)
    
    string_note_input = "Please enter note you want to practice, be sure to include sharps or flats as # or b repectively if desired or type 'random': "
    print(string_note_input)
    requested_note = str(input())

    if requested_note.lower() == 'random':
        requested_note = requested_note.lower()
    requested_note = requested_note.capitalize()

    for note in notes:
        if requested_note == note:
    

    string_mode_input = "Please enter the mode that you want to practice or type 'Random' for randomized selection: "
    print(string_mode_input)
    requested_mode = str(input())
    requested_mode = requested_mode.lower()


if __name__ == '__main__':
    main()
