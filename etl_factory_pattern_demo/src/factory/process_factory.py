from ..processes import processes


class ProcessFactory:
  registry={}

  def load_processes(self):
    for process in processes:
      self.registry.update({process.__name__.lower(): process})



if __name__ == "__main__":
  factory = ProcessFactory()

  factory.load_processes()

  print(factory.registry)