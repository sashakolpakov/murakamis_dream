# The Gauss-wall flux gives the actual peripheral character

Research proof, 27 October 2026. The physical compact source and its
exceptional divisor cannot be identified by a fixed-complete-meridian
homotopy avoiding the Gauss pole. Their difference has an explicit
tube class. Varying the meridian transfers this flux into a peripheral
period. Its inverse exponential is exactly the retained Frobenius
character at the actual roots, including the square-root sign in the
full ADO normalization.

There is also a global rational primitive for the principal Gaussian
Haar adapter. It keeps the polar boundary co-source rather than
discarding the adapter or changing the cycle.

The geometric cycle calculation is developed independently in
[the meridian homotopy note](meridian_homotopy_wall_and_source_residues.md).
The fixed-cycle obstruction and its Gysin interpretation are in
[the Gauss-wall cycle audit](gauss_wall_cycle_and_peripheral_flux.md).
No selected-volume estimate follows from the polar character alone.

## 1. The fixed-cycle obstruction

Use the actual resolved frame space

    Y=Tot(O_P1(-2)) times_P1 X, E={eta=0},
    X=Conn(O(1)), Omega=dv wedge da.

Its charts have V=1/v, eta'=-v^2 eta, a'=v-v^2a.
The physical matrix entry

    F=mu_11=1-eta v=1+eta'V

is a global function. Its zero divisor D is G_m,v times A^1,a.
Keeping the south plus sign is essential: using 1-eta'V would
select the other diagonal entry of the meridian.

Write c=2pi*i and T=va. The physical compact section is

    eta_phys=(1-exp(-cT))/v,
    F_phys=exp(-cT).

It extends at both real compact poles as already proved. On the
real sphere Gamma, T ranges from zero to one and

    integral_(angle) Omega=-c dT.

The global closed two-form on Y minus D

    Xi=dlog F wedge dlog v=dv wedge d eta/F

has residue dlog v on D. On the physical section it equals
c Omega, and on E its restriction is zero. Therefore

    integral_(Gamma_phys) Xi=-c^2=4pi^2,
    integral_(Gamma_E) Xi=0.                           (1)

Thus the cycles are not homologous in Y minus D. The normal
radial interpolation eta_lambda=lambda eta_phys has

    F_lambda=(1-lambda)+lambda exp(-cT).

It meets D at lambda=T=1/2 along the full angle circle

    v=exp(i phi), a=1/(2v), eta=1/v.

The local expression F=-2(lambda-1/2)+pi*i(T-1/2)+higher
terms fixes the intersection sign. With the marked normal-circle
orientation the actual relation is

    [Gamma_phys]-[Gamma_E]=-Tube[gamma_v],
    integral_(Tube gamma_v) Xi=c^2.                     (2)

This is an actual nonzero correction. A chartwise exponential
interpolation avoids F=0 only by violating its other-chart clutch;
its missing factor is exp(-c lambda). It is not a global fixed-
meridian replacement for (2).

## 2. The Haar adapter has an explicit global relative primitive

Let theta=-a dv be a local source connection, so dtheta=Omega and
theta'=theta+dlog v. On Y minus E define

    vartheta=dlog eta-2theta=dlog eta+2a dv.

The chart transitions cancel, making vartheta global, and
d vartheta=-2Omega. The two actual principal three-forms are

    H_G=-dlog eta wedge Omega,
    H_cut=H_G/F.

The factor 1/F is exactly the interior adapter of the actual
Gaussian/flag calculation. Direct exterior differentiation gives

    H_cut-H_G=dlog F wedge Omega=dB,
    B=(1/2)dlog F wedge vartheta
      =(1-2va)d eta wedge dv/(2F).                       (3)

Although the first expression for B uses vartheta, the second
shows that B is regular along E. It has poles only on D. In the
south chart the same form is

    B=(2Va'-1)d eta' wedge dV/(2F).

The identity (3) therefore is global, not just an affine primitive.
Its boundary residue is

    Res_D B=(a-1/(2v))dv,
    -d Res_D B=Omega=Res_D(H_cut-H_G).                    (4)

On the radial intersection circle in (2), this one-form vanishes.
The pullback of B to the physical sphere is
-(1-2T)Xi/2, whose compact period is zero. These facts explain
the ordinary principal current calculation but do not remove
the nonzero two-cycle charge (1).

There is an exact marked-logarithm correction as well. Radial
integration of H_cut-H_G gives Log_chord(F_phys)Omega. The log
followed along the straight chord is -cT for T<1/2 and c(1-T)
for T>1/2, so its compact period is zero. The actual physical
mark Log F_phys=-cT differs by -c on the upper half. Its added
relative period is

    (-c) integral_(T>1/2)Omega=c^2/2=-2pi^2.              (5)

At H_N=c/N its exponential is exp((c^2/2)/H_N)=(-1)^N.
Equation (5) computes a marked relative-period phase. Realizing
that phase as a multiplier of the actual quantum word requires
the source/action map; it is not inferred from the classical
primitive. The separate half-form and ribbon characters remain.

## 3. The peripheral period and its orientation

The globally regular eigenvalue-varying orbit family is described
in the meridian homotopy note. Its preferred eigenvalue is m and
the actual inverse-eigenvalue convention is M=m^(-1). With that
note's fixed orientation, its compact Gauss period is

    I_phys(M)=2c Log M.

It changes from zero to -c^2 along M=exp(-pi*i lambda),
lambda=0,...,1. For the convenient inverse-source character below,
take the opposite oriented flux

    I_inv(M)=-2c Log M.                                  (6)

This inversion is explicit; no cycle orientation is silently reset.
Both periods must be kept on the marked meridian logarithm torsor.
The peripheral Cech transition records the same flux via the
actual change of eigenvalue. Its endpoint lift is M=-1, so the
original SL2/peripheral character remains part of the comparison.

## 4. Its inverse character is exactly the actual Frobenius coordinate

Keep H=Log Q, q=exp(H/2), and define on that logarithmic torsor

    chi_H(M)=exp[I_inv(M)/H]
            =exp[-2c Log M/H].                          (7)

The actual meridian half-step sends Log M to Log M+H/2. Thus

    chi_H(qM)=chi_H(M),
    chi_H^(1/2)(qM)=-chi_H^(1/2)(M).                     (8)

The square root here is the marked exponential exp(-c Log M/H),
not an independently chosen algebraic root. At the actual level,

    H_N=c/N, chi_(H_N)(M)=M^(-2N),
    chi_(H_N)^(1/2)(M)=M^(-N).                         (9)

The direct character from I_phys is its inverse U=M^(2N).
Hence the geometric wall flux recovers precisely the full retained
central power coordinate of the actual root object.

The whole period line has connection

    dlog chi_H=-2c dLogM/H+2c LogM dH/H^2.                (10)

It is a horizontal period object with a marked logarithm, not a
claim of rationality in Q,M. A log deck shift LogM->LogM+c
multiplies it by exp(-2c^2/H). This equals one at every H_N but
has first logarithmic-Q derivative 2N^2 there. Thus root values
alone forget a nonzero quantum jet. This is a direct period
calculation, not yet an identification with the actual first-normal
connection of a chosen quantum A-module.

## 5. The full modified dimension is its actual polar adapter

Let kappa=M-M^(-1) and retain the original epsilon_N=i^(N+3).
The independently fixed full ADO normalization is exactly

    d_N(M)=epsilon_N kappa/(M^N-M^(-N))
          =epsilon_N kappa chi_(H_N)^(1/2)/(1-chi_(H_N)). (11)

This includes its square-root sign and whole meridian divisor.
It follows directly from (9), with no normalization fitted to
volume. Its q half-step ratio is

    d_N(qM)/d_N(M)=-kappa(qM)/kappa(M),                    (12)

the exact recorded character of the full period. Under meridian
inversion chi becomes chi^(-1) and kappa changes sign, leaving
(11) unchanged. At M=1 its whole canceled value is epsilon_N/N.
The exact Weyl scalar is (N/epsilon_N)d_N(M), as proved in
[the balanced Weyl calculation](twisted_cotangent_source_and_weyl_gluing.md).

Equation (11) is an equality at the actual quantum roots, with
all meridian dependence retained. The geometric H-dependent lift
(7) is not asserted to equal a chosen auxiliary off-root finite-
matrix source. Its quantum-normal comparison, including (10),
still needs to be proved. Only its root restrictions and their
actual meridian half-step character are identified here.

## 6. The actual wall charges have a polynomial budget

On M(lambda)=exp(-pi*i lambda), equation (11) is

    d_N=epsilon_N sin(pi lambda)/sin(pi N lambda).

Its possible interior simple walls are lambda=k/N, 1<=k<N.
The actual reduced state at that meridian is C_k(q_N), by the
proved root-color identity and meridian reciprocity. Therefore

    Res_(lambda=k/N)[d_N(M)F_N(M^2)d lambda]
       =epsilon_N (-1)^k sin(pi k/N) C_k(q_N)/(pi N).     (13)

A vanishing C_k makes the wall removable. The original positive
ordinary-color trace bound |C_k(q_N)|<=D_N gives

    sum_(k=1)^(N-1)|2pi*i Res_k|<=2D_N.                  (14)

Thus these actual polar charges are polynomially bounded for a
fixed knot braid. Their phases and SL2 endpoint character remain
specified. A transport kernel multiplies each charge by its wall
value; (14) is not a bound for an unspecified kernel or an identity
expressing the Kashaev point value as this meridian integral.

## 7. What is still missing

The global wall current, its peripheral flux, the actual central
character, and its polar source adapter now agree with explicit
marks and signs. The eigenvalue-varying geometric detour also has
a source-current transport in
[the exponential Cech construction](compact_exponential_cech_current_detour.md).
That transport lives in a holomorphic/exponential-period extension
of the algebraic source complex. It is not automatically an
intertwiner of the actual quantum clock or star product.

The knot-dependent regular part of the full period is still not
determined by the wall charges. The exact decomposition in
[the regularized ADO theorem](regularized_kashaev_period.md) retains
it as R_N, with K_N=N R_N(1)+P_N(1) and P_N(1) polynomially bounded.
The volume norm belongs to that selected regular sector. A source-
preserving comparison of the whole quantum word or A-object with
the marked geometric regulator, and its large-level norm control,
remain unproved.

Verification: [audit script](../experiments/audit_gauss_wall_peripheral_character.py)
and [results](../experiments/gauss_wall_peripheral_character_results.json)
check the global rational primitive, marked phases, whole half-step
character, root normalization and 91 actual polar-residue conventions.

The later [integral-color frame calculation](quantum_factorial_frames_and_cyclotomic_source.md)
does match the principal clock by moving q and the integral color
together. Its symmetric frame has a regular sphere twist; the
inverse eigenflag retains two boundary bubbles. This is not an
off-root identification of the generic-M finite root source or
its quantum-normal connection.
