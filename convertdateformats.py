import numpy as np
import re
import datetime
import pandas as pd
from time import strptime

def nearestDate(items, pivot): # pivot is the date? 
    """ Add description of this function 
    """
    return min(items, key=lambda x: abs(x - pivot))

# def allowableformats():
#     dtformats = {'datetime.date':str(datetime.time),'datetime.datetime':str(datetime.datetime),
#         'pd.Timestamp':str(pd.Timestamp),'np.datetime64':str(np.datetime64),'str':str(str)}
#     return(dtformats)

class datetimeconvert:
    """
    Class for converting between datetime.date, datetime.datetime, pd.Timpstamp and np.datetime64 formats.
    This class can also convert datetime strings to the listed formats if an exceptable strformat is passed.
    This is mainly required when data is read in from a csv file
    """

    def allowableformats():
        dtformats = {'datetime.date':str(datetime.time),'datetime.datetime':str(datetime.datetime),
            'pd.Timestamp':str(pd.Timestamp),'np.datetime64':str(np.datetime64),'str':str(str)}
        return(dtformats)

    def allowablestrformats():
        """
        Creates a dictionary of allowable datetime string formats (that go between delimiters)
        """
        yeard = ['yyyy','yy']
        monthd = ['mm','m','MMM','Mmm','monthname'] # monthname must not contain an uppercase 'T'
        dayd = ['dd','d']
        hourd = ['hh','h']
        minuted = ['nn','n'] # use n's because m's already used for month
        secondd = ['ss','s','ss.ss'] # can specify ss.ss to any level of precision 

        return({'year':yeard,'month':monthd,'day':dayd,'hour':hourd,'minute':minuted,'second':secondd})

    def __init__(self,x,informat,outformat,strformat): # *args
        """
        May need to bring self.dtformats, self.datetimestrs outside of the__init__
        the allowableformats & allowablestrformats will work for now
        """
        self.x = x # input date/datetime/str to be converted
        self.informat = informat
        self.outformat = outformat
        self.strformat = strformat 
        # self.getstrinfo = self.getstrinfo()

        dtformats = {'datetime.date':str(datetime.time),'datetime.datetime':str(datetime.datetime),
        'pd.Timestamp':str(pd.Timestamp),'np.datetime64':str(np.datetime64),'str':str(str)}

        self.dtformats = dtformats # may need to bring outside init function
        # self.dtformats = allowableformats() # want to be able to call as function

        def maketypesdict():
            """
            Creates a dictionary of allowable datetime string formats (that go between delimiters)
            """
            yeard = ['yyyy','yy']
            monthd = ['mm','m','MMM','Mmm','monthname'] # monthname must not contain an uppercase 'T'
            dayd = ['dd','d']
            hourd = ['hh','h']
            minuted = ['nn','n'] # use n's because m's already used for month
            secondd = ['ss','s','ss.ss'] # can specify ss.ss to any level of precision 

            return({'year':yeard,'month':monthd,'day':dayd,'hour':hourd,'minute':minuted,'second':secondd})

        datetimestrs = maketypesdict()
        self.datetimestrs  = datetimestrs # may need to bring outside init function
    
    # class getstrinfo:
    #     """ How to get r variable out of the functions to avoid double up in code?
    #     """
    # def allowableformats():
    #     return(dtformats)

    def get_rpattern(self):
        return(re.compile(r"[^a-z,A-S,U-Z,.]"))

    def getstrdelims(self):
        r = self.get_rpattern()
        return(re.findall(r,self.strformat))

    def getstrvalues(self):
        r = self.get_rpattern()
        return(r.sub(',',self.strformat).split(','))

    def checkdelims(self):
        """ Check if the input for conversion has valid delimiters
        """
        
        delims = re.sub(r'\d','',str(self.x))
        invaliddelim = [] # list of invalid characters
        outstr = ""

        for i in delims:
            if type(i) == int:
                invaliddelim.append(i)

            elif i.isalnum():
                if i == 'T': # 'T' is a valid delimiter character 
                    pass
                else:
                    invaliddelim.append(i)

            elif i == '.':
                invaliddelim.append(i)

            else:
                # print(i, 'pass')
                pass

            if len(invaliddelim) == 0:
                outstr += 'All delimiters are valid'
            elif len(invaliddelim) != 0:
                outstr += 'Input contains invalid delimiters: %s' % invaliddelim

            return(outstr)

    # def checkstrformat(self):
    # Need to build this function 
    #     """ Strip the delimiters from the input string and make sure there are no characters that can't be used
    #     """
    #     unqdelim = np.unique(np.array(self.getstrinfo.getstrdelims()))
    #     for i in unqdelim():
    #         if i in 


    #     return()


    def checkdataformat(self):
        """ Function for checking that the input and output formats for the conversion are compatible with this program
        """
        informat = self.informat
        outformat = self.outformat
        alformat = self.dtformats.keys()
        outstr = ""

        if informat in alformat:
            outstr += 'Input format: %s okay & ' % self.dtformats[informat]
        elif informat not in alformat:
            outstr += 'Unrecognized input format &'

        if outformat in alformat:
            outstr += 'Output format: %s okay' % self.dtformats[outformat]
        elif outformat not in alformat:
            outstr += 'Unrecognized output format'
        return(outstr)
        
    def maketypeassociation(self):
        """ # make dictionary associating any exceptable delimiter with a type 
        """
        types = self.datetimestrs 
        dict_vtypes = {}
        for t in types:
            for i in types[t]:
                dict_vtypes[i] = t
        return(dict_vtypes)

    def dtstr2dtdict(self):
        """
        """

        dtime = self.x
        strf = self.strformat

        dict_vtypes = self.maketypeassociation()

        # dictionary of values to output 
        dict_dt = {}

        # delims = self.getstrinfo.getstrdelims(self)
        delims = self.getstrdelims()

        # strvalues = self.getstrinfo.getstrvalues(self)
        strvalues = self.getstrvalues()

        # return(strvalues)
        
        

        # use a list of delimiters to get list of ymdhms values
        # unqdelim = np.unique(np.array(delims))
        # pattern = "[%s]" % (',').join(unqdelim)
        pattern = "[%s]" % (',').join(delims)
        a = re.compile(r'%s' % pattern)
        tvalues = a.sub(',',dtime).split(',')

        # return{'delims':delims,'pattern':pattern,'a':a,'tvalues':tvalues}
        # return(tvalues)
        for i in range(0,len(strvalues)):

            t = strvalues[i] # 
            v = tvalues[i]
            ttype = dict_vtypes[t]

            # format year
            if ttype == 'year':
                if len(str(v)) == 2: # short format year
                    yr = '20%s' % v
                else:
                    yr = v

                dict_dt[ttype] = str(yr)

            # format month
            if ttype == 'month':
                if len(t) < 3:
                    mn = v
                elif len(t) == 3:
                    # print(v,t)

                    v = str(v).lower()
                    mn = strptime(v,'%b').tm_mon
                else:
                    v = str(v[:3]).lower()
                    # print(v)
                    mn = strptime(v,'%b').tm_mon

                dict_dt[ttype] = str(mn)

            # format day, hour, minute, second
            dhms = ['day', 'hour', 'minute', 'second']
            if ttype in dhms:
                dict_dt[ttype] = v           

        return(dict_dt)

    def input(self):
        print(self.x)


    def convertdtformat(self):
        """ can specify string format as None 
        """
        x = self.x
        informat = self.informat
        outformat = self.outformat
        strformat = self.strformat

        if informat == 'datetime.date':
            yr, mn, d = x.year, x.month, x.day
            h, m, s = 0, 0, 0 # abritrayily set to 0,0,0

        elif informat == 'datetime.datetime' or informat == 'pd.Timestamp':
            yr, mn, d = x.year, x.month, x.day
            h, m, s = x.hour, x.minute, x.second

        elif informat == 'np.datetime64':
            # extract data from string, use default np.datetime64 format 
            self.x = str(x)
            self.strformat = 'yyyy-mm-ddThh:nn:ss.ss' # use n's because m's already used for month

            dtimeinfo = self.dtstr2dtdict()
            yr, mn, d = dtimeinfo['year'], dtimeinfo['month'], dtimeinfo['day']
            h, m, s = dtimeinfo['hour'], dtimeinfo['minute'], dtimeinfo['second']

        elif informat == 'str':
            # extract data from string
            self.x = str(x)
            dtimeinfo = self.dtstr2dtdict()
            yr, mn, d = dtimeinfo['year'], dtimeinfo['month'], dtimeinfo['day']

            if len(dtimeinfo.keys()) == 3:
                h, m, s = 0, 0, 0 # abritrayily set to 0,0,0
            else:
                h, m, s = dtimeinfo['hour'], dtimeinfo['minute'], dtimeinfo['second']

        if outformat == 'datetime.date':
            outvalue = datetime.date(int(yr),int(mn),int(d))

        elif outformat == 'datetime.datetime':
            yr,mn,d,h,m = int(yr), int(mn), int(d), int(h), int(m)
            s = int(round(float(s),0)) # round float value as dtype requires int value 
            outvalue = datetime.datetime(yr,mn,d,h,m,s)

        elif outformat == 'pd.Timestamp':
            yr,mn,d,h,m = int(yr), int(mn), int(d), int(h), int(m)
            s = int(round(float(s),0)) # round float value as dtype requires int value 
            outvalue = pd.Timestamp(yr,mn,d,h,m,s)

        elif outformat == 'np.datetime64':
            tstr = '%s-%s-%sT%s:%s:%s' % (str(yr).zfill(4),str(mn).zfill(2),str(d).zfill(2),str(h).zfill(2),str(m).zfill(2),str(s).zfill(2))
            outvalue = np.datetime64(tstr)

        return(outvalue)

if __name__ == "__main__":
    datetimeconvert
