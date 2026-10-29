# The finite Fourier cap keeps the physical clock and band character independent

Exact source theorem and category audit, 27 October 2026. A four-port
head tensor has a literal band-Fourier cap, with an exact finite root
average. That average does not sum the physical position index and
does not substitute a geometric wave momentum for its Fourier variable.
Unwrapped tails retain explicit alias norm characters.

## 1. The actual selected functional

Let R be the original coefficient algebra over the marked cyclotomic
field Q(zeta), where zeta is a primitive N-th root. The actual whole
Q/M variables, phases, pivots,
caps, peripheral factors and normal parameters may all remain in R.
The Fourier sampling root zeta is held fixed; Q need not equal zeta
before its actual root specialization.

For the literal port ordering write

    J^(p,q)_(a,b)=T_(a+p,b+q;a,b),
    F_T(x,y;xi,eta)=sum J^(p,q)_(a,b) x^a y^b xi^p eta^q.

All four head indices lie in [0,N-1] before zero extension. Therefore
|p|,|q|<N. The original balanced first cut and identity second closure
give EXACTLY

    Phi(T)=(1/N)[eta^0]F_T(1,1;1,eta)
          =(1/N)sum_(a,b,p) J^(p,0)_(a,b).        (1)

This uses every first-port band. It is not restricted to the scalar
double diagonal when acting on off-diagonal Ward current tensors.
There is only the original physical normalization 1/N.

For any retained physical input-clock insertion f(Q^b), the same
formula holds with that factor inside the sum. The following identities
are R-linear, so every original factor and every whole normal derivative
is preserved coefficientwise.

## 2. Exact finite Fourier theorem and all tail corrections

For any finite Laurent polynomial F(eta)=sum_q F_q eta^q over R,
orthogonality of the finite characters proves

    Av_N(F):=(1/N)sum_(j=0)^(N-1) F(zeta^j)
            =sum_(k in Z) F_(kN),

    [eta^0]F=Av_N(F)-sum_(k!=0) F_(kN).           (2)

Proof: sum_j zeta^(jq) is N if N divides q and zero otherwise.
Every sum is finite. In particular, on the ENTIRE original head-band
space |q|<N,

    Phi(T)=(1/N^2)sum_(j=0)^(N-1)
                         F_T(1,1;1,zeta^j).       (3)

The extra 1/N here is the Fourier averaging factor. It does NOT turn
the physical b sum into a normalized second trace; y=1 and all b
coefficients remain in each summand. Dropping that sum changes (1).

For a shifted/moment current eta^ell D_eta^h F, where
D_eta=eta partial_eta, the exact version is

    [eta^0](eta^ell D_eta^h F)
      =(-ell)^h F_(-ell)
      =Av_N(eta^ell D_eta^h F)
         -sum_(k!=0)(kN-ell)^h F_(kN-ell).        (4)

For h=0 the factor is one. Arbitrary polynomial index moments and
whole rational coefficients may instead be included directly in F_q.
Their monodromy factors are not replaced by root values in doing so.
Equations (2) and (4) keep precisely the aliases of unwrapped
Green/divided tails. A high-color head of dimension greater than N
also need not have |q|<N, so its aliases must be retained even if
all of its own ports are physically head-supported.

There is a useful WHOLE version that does not collapse these tails.
Adjoin independent V_eta and v with v^N=V_eta. Then

    Av_(N,V_eta)(F):=(1/N)sum_j F(v zeta^j)
                    =sum_k F_(kN) V_eta^k,
    [eta^0]F=[V_eta^0] Av_(N,V_eta)(F).            (5)

This is also the normalized multiplication trace in the free cyclic
algebra R[V_eta^+-1][eta^+-1]/(eta^N-V_eta). Setting V_eta=1
FIRST merges all aliases. Keeping V_eta independently recovers the
literal unwrapped cap, its endpoints and all moment factors.

## 3. The physical position clock is a different coordinate

The whole physical input clock B=Q^b acts on F_T by y->Qy.
The output clock Q^(b+q) acts by

    (y,eta)->(Qy,Qeta).                            (6)

Thus Q^b and eta are independent. The eta dilation is only the
OFFSET part of the output clock, not the input physical clock or
its sum. These formulas are direct index equalities before Q^N=1.
If a cyclic presentation is used for both variables, keep separate
power coordinates U_B=B^N and V_eta=eta^N. Equality of some root
values does not identify their normal germs: D_Q U_B=Nb U_B,
while a fixed Fourier sampling value V_eta has no such derivative.

For the literal two-cut unknot, T is the flip tensor. Therefore

    F(eta)=sum_(q=-(N-1))^(N-1)(N-|q|)eta^q,
    Phi(T)=1.

The finite Fourier average is N, followed by the ORIGINAL 1/N.
With an input-clock insertion f(Q^b), the selected value is
(1/N)sum_b f(Q^b). In particular at Q=zeta the insertion f(B)=B
has value zero, whereas retaining only b=0 has value 1/N. This
actual tensor distinguishes the physical sum from the Fourier cap.

The exact orientation-cover identity
F(eta)deta/eta=[(eta-eta^-1)F]du/(u^2-4), u=eta+eta^-1,
remains a source-preserving rational identity, including its marked
eta=0 sheet. It does not identify eta with a physical position.

## 4. Bounded phase ratios do not turn the cap into substitution

The bounded-band Gaussian theorem gives, for each FIXED offset q,
a principal ratio Z_q/Z_0=p_e^q with the specified actual frame.
After Fourier generation, this is the principal character-incidence
relation eta p_e=1. It is not an equality of the two bases and not
an instruction to evaluate a finite kernel at eta=p_e^-1.
Summing offsets growing with N also requires information not supplied
by a theorem for each fixed bounded offset.

There IS a precise positive bounded-test consequence. If h(eta) is a
fixed Laurent polynomial, source pairing selects only its finitely
many opposite bands:

    [eta^0](h(eta) sum_q Z_q eta^q)/Z_0
       =sum_j h_j Z_(-j)/Z_0 -> h(p_e^-1).        (7)

Thus the principal source distribution evaluates BOUNDED TESTS at the
incidence point. Equation (7) neither evaluates the entire growing
kernel there nor transports the original contour/endpoint. Higher
terms act by derivatives on h; the complete finite source still uses
all bands and aliases. This distinguishes distributional pairing from
the false kernel-substitution inference below.

There is an exact finite-port obstruction to inferring substitution
from the ratios alone. Put T_(0,q;0,0)=p_e^q for 0<=q<N, and
all its other port entries zero. This is a valid element of the
same finite four-port tensor space, with generating kernel

    K_N(eta)=sum_(q=0)^(N-1)(eta p_e)^q.

It has the phase ratio p_e^q EXACTLY. Its actual cap is
[eta^0]K_N=1, while K_N(p_e^-1)=N. No scalar correction can
make substitution equal the cap on both this kernel and the
constant kernel one. This is an obstruction to a universal
co-source inference, not a counterexample about a knot invariant.

Consequently one may define a SEPARATE geometric coordinate
eta_geo=p_e^-1 and compute its rational Jacobian, boundary values
or residues. None of those calculations alone transports the
original Fourier cap eta=0, its finite contour/root average or
its full tails into eta_geo. A source-compatible Fourier/canonical
pushforward is still required.

## 5. Consequence for the existing boundary calculations

Sections 1--5 of
[the identity-cut orientation note](identity_cut_orientation_cover_and_marked_source.md)
are exact finite source identities. Its geometric equations remain
valid when eta is read there as the independent chart coordinate
eta_geo=p_e^-1. The phrases saying that the ORIGINAL cap eta=0
therefore reaches B=1 require this unproved source pushforward.
They must not be used as a deduction from a principal ratio or
an equality of two rational one-forms alone.

Likewise the
[actual first-loop calculation](figure_eight_first_loop_cap_residue.md)
and its Hermite certificate remain exact statements about the
actual transverse Gaussian on the candidate geometric boundary
eta_geo. Its zero residues and nonzero relative endpoint gaps
are not thereby the image of the finite Fourier cap functional.
The [independent first-loop audit](wick_first_loop_actual_atom_independent_audit.md)
retains this distinction explicitly.

[Exact head/tail/clock checks](../experiments/audit_finite_band_fourier_cap.py)
and [saved results](../experiments/finite_band_fourier_cap_results.json).
The checks pass at seven levels N=2,...,8: all 8,771 literal
four-port units, 5,544 shifted-moment tail cases, 203 independent
input/output clock units, the actual two-cut unknot with its
input-clock insertion, and the exact character-kernel obstruction.
Generic Q values and the fixed Fourier sampling root are tested
separately.
