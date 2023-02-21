# NOTE: This file is auto generated by OpenAPI Generator 6.5.0-SNAPSHOT (https://openapi-generator.tech).
# Do not edit this file manually.

defmodule OpenapiPetstore.Model.Cat do
  @moduledoc """
  
  """

  @derive [Poison.Encoder]
  defstruct [
    :className,
    :color,
    :declawed
  ]

  @type t :: %__MODULE__{
    :className => String.t,
    :color => String.t | nil,
    :declawed => boolean() | nil
  }
end

defimpl Poison.Decoder, for: OpenapiPetstore.Model.Cat do
  def decode(value, _options) do
    value
  end
end

