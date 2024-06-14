from herramientas_red import EscanerRed, MonitorRed

if __name__ == "__main__":
    # Creando las instancias de las clases
    escaner = EscanerRed()
    monitor = MonitorRed()

    # Llamada a los métodos de las clases
    escaner.esc_red()
    monitor.monit_trafico()