from sqlalchemy import Column, Integer, String, Date
from cap.db import Base, engine


class Balloons(Base):
    __tablename__ = "balloons"

    uid = Column(Integer, primary_key=True)
    firm = Column(String())
    paint_code = Column(String())
    color = Column(String())
    volume = Column(String())
    weight = Column(Integer)
    created_at = Column(Date())
    updated_at = Column(Date())

    def __repr__(self) -> str:
        return f"Balloons {self.uid} {self.firm} {self.paint_code} {self.color} {self.volume} {self.weight} {self.created}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)