class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            with open(self.name, "r") as my_file:
                my_file.readline()
        except FileNotFoundError:
            raise ExamException("Errore, file non esistente")
        except IOError:
            raise ExamException("Errore, file non leggibile")
        
        with open(self.name, "r") as my_file:
            data = []
            timestamps = []
            for line in my_file:
                if not line:
                    continue

                elements = line.split(",")
                elements[-1] = elements[-1].strip()

                if "-" not in elements[0]:
                    continue
                else:
                    try:
                        anno_mese = elements[0].split("-")
                        int(anno_mese[0])
                        int(anno_mese[1])
                    except ValueError:
                        continue
                    
                if elements[0] in timestamps:
                    raise ExamException("Errore, timestamp duplicato")
                if timestamps and elements[0] < timestamps[-1]:
                    raise ExamException("Errore, timestamp fuori ordine")
                elif elements[0] != "date":
                    data.append(elements)
                    timestamps.append(elements[0])
        return data

def compute_increments(time_series, first_year, last_year):
    first_valido = False
    last_valido = False
    for i in range(len(time_series)):
        if first_year in time_series[i][0]:
            first_valido = True
        if last_year in time_series[i][0]:
            last_valido = True
    if first_valido is False or last_valido is False:
        raise ExamException("Errore, estremo/i dell'intervallo non validi")

    medie = []
    for i in range(int(first_year), int(last_year) + 1):
        pass_anno = []
        for j in range(len(time_series)):
            if str(i) in time_series[j][0]:
                try:
                    converted_value = float(time_series[j][1])
                except ValueError:
                    continue
                if time_series[j][1] == "":
                    continue
                if converted_value <= 0:
                    continue
                else:
                    pass_anno.append(converted_value)
        if len(pass_anno) != 0:
            media = sum(pass_anno) / len(pass_anno)    
            medie.append([str(i), media])
        else:
            continue

    incrementi = {}
    for k in range(len(medie) - 1):
        diff_medie = medie[k + 1][1] - medie[k][1]
        incrementi[str(medie[k][0]) + "-" + str(medie[k + 1][0])] = diff_medie
        
    return(incrementi)