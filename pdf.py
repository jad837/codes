import math
class p:
    stdev = 34
    mean = 180
    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        n=math.exp( -((x-self.mean)**2)   )/ (2* (self.stdev **2))
        d = self.stdev*(math.sqrt(2*math.pi))
        #return n/d
        return (1.0 / (self.stdev * math.sqrt(2* math.pi) ))*math.exp(-0.5*((x-self.mean)/self.stdev)**2) 

pre = p()
print(pre.pdf(120)+pre.pdf(155))
print(math.exp(-25)/(2*(34**3)*math.sqrt(2*math.pi)))