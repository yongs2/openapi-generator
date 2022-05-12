#
# OpenAPI Petstore
# This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: "" \
# Version: 1.0.0
# Generated by OpenAPI Generator: https://openapi-generator.tech
#

<#
.SYNOPSIS

No summary available.

.DESCRIPTION

No description available.

.PARAMETER Var123List
No description available.
.OUTPUTS

List<PSCustomObject>
#>

function Initialize-PSList {
    [CmdletBinding()]
    Param (
        [Parameter(Position = 0, ValueFromPipelineByPropertyName = $true)]
        [String]
        ${Var123List}
    )

    Process {
        'Creating PSCustomObject: PSPetstore => PSList' | Write-Debug
        $PSBoundParameters | Out-DebugParameter | Write-Debug


        $PSO = [PSCustomObject]@{
            "123-list" = ${Var123List}
        }


        return $PSO
    }
}

<#
.SYNOPSIS

Convert from JSON to List<PSCustomObject>

.DESCRIPTION

Convert from JSON to List<PSCustomObject>

.PARAMETER Json

Json object

.OUTPUTS

List<PSCustomObject>
#>
function ConvertFrom-PSJsonToList {
    Param(
        [AllowEmptyString()]
        [string]$Json
    )

    Process {
        'Converting JSON to PSCustomObject: PSPetstore => PSList' | Write-Debug
        $PSBoundParameters | Out-DebugParameter | Write-Debug

        $JsonParameters = ConvertFrom-Json -InputObject $Json

        # check if Json contains properties not defined in PSList
        $AllProperties = ("123-list")
        foreach ($name in $JsonParameters.PsObject.Properties.Name) {
            if (!($AllProperties.Contains($name))) {
                throw "Error! JSON key '$name' not found in the properties: $($AllProperties)"
            }
        }

        if (!([bool]($JsonParameters.PSobject.Properties.name -match "123-list"))) { #optional property not found
            $Var123List = $null
        } else {
            $Var123List = $JsonParameters.PSobject.Properties["123-list"].value
        }

        $PSO = [PSCustomObject]@{
            "123-list" = ${Var123List}
        }

        return $PSO
    }

}

