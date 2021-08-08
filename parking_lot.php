<?php

class ParkingLot
{
  private $address;
  private $parkingSpots;

  public function __construct(string $address, array $parkingSpots)
  {
    $this->address = $address;
    $this->parkingSpots = $parkingSpots;
  }

  public function getAddress()
  {
    return $this->address;
  }

  public function getParkingSpots()
  {
    return $this->parkingSpots;
  }
}

class ParkingSpot
{
  const SIZE_COMPACT = 'compact';
  const SIZE_REGULAR = 'regular';
  const SIZE_LARGE = 'large';

  const PARKING_SPOT_SIZES = [
    self::SIZE_COMPACT,
    self::SIZE_REGULAR,
    self::SIZE_LARGE
  ];

  private $size;
  private $price;
  private $parkingLot;
  private $level;
  private $takenFrom;
  private $takenTo;

  public function __construct(string $size, float $price, ParkingSpot $parkingSpot, int $level, DateTime $takenFrom, DateTime $takenTo)
  {
    $this->size = $size;
    $this->price = $price;
    $this->parkingSpot = $parkingSpot;
    $this->level = $level;
    $this->takenFrom = $takenFrom;
    $this->takenTo = $takenTo;
  }

  //... getters and setters
  public function isAvailable(): bool
  {
    $now = new DateTime();
    
    if ($now > $this->takenTo) {
      return true;
    }

    return false;
  }
}

class User {
  private $cars;

  public function __construct(array $cars)
  {
    $this->cars = $cars;
  }
  
  //... getters and setters
}

class Car {
  const SIZE_COMPACT = 'compact';
  const SIZE_REGULAR = 'regular';
  const SIZE_LARGE = 'large';

  const PARKING_SPOT_SIZES = [
    self::SIZE_COMPACT,
    self::SIZE_REGULAR,
    self::SIZE_LARGE
  ];

  private $size;
  private $licensePlate;
  private $user;

  public function __construct(string $size, string $licensePlate, User $user)
  {
    $this->size = $size;
    $this->licensePlate = $licensePlate;
    $this->user = $user;
  }
  
  //... getters and setters
}
