<?php
namespace App;

interface NotifierInterface {
    public function send(Task $task): void;
}
