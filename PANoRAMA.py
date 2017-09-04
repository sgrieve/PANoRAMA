from PIL import Image


class panorama():
    def __init__(self, infile, step, duration, loop):
        '''

        '''
        # Load animation settings
        self.step = step
        self.duration = duration
        self.loop = loop

        # Load the input file and get its geometry
        self.input = Image.open(infile)
        self.width, self.height = self.input.size
        self.final_width = int(self.height * 1.5)

        # Create the animation frames
        self.frames = []
        self.process()

    def load(self):
        '''
        Method to contain the error handling of file loading
        '''
        pass

    def process(self):
        '''

        '''
        for i in range(0, self.width - self.final_width, self.step):
            self.frames.append(self.input.crop((i, 0, self.final_width + i,
                                                self.height)))

        # This leaves a black screen at the end of each loop
        # self.frames = self.frames + self.frames[::-1]

        # This second loop should be replaced by the slicing above
        for i in range(self.width - self.final_width, 0, -self.step):
            self.frames.append(self.input.crop((i, 0, self.final_width + i,
                                                self.height)))

    def save(self, outfile):
        '''

        '''
        output = Image.new(self.input.mode, (self.final_width, self.height))
        output.save(outfile, save_all=True, append_images=self.frames,
                    duration=self.duration, loop=self.loop)

pan = panorama('input.jpg', 100, 20, 0)

pan.save('classtest.gif')
