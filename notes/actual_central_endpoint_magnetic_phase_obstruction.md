# What simplifies at the geometric endpoint, and a magnetic gauge obstruction

30 October 2026. At every ODD level, fixing all complete-circle
channels to the genuine simple endpoint makes each retained half twist
an explicit scalar. The local q-Hahn critical equation also has no
saddle collision on its physical endpoint domain. Nevertheless the
actual central black spin tensor cannot be made entrywise positive
by separate nonzero gauges on its three magnetic legs, already at N=3.

The obstruction is an exact gauge-invariant six-entry ratio. It does
not rule out a larger coherent resummation or a positive final scalar.
It identifies why selecting endpoint channels and adjusting separate
leg phases is not itself a general positive-source proof.

## 1. All retained half twists become known endpoint scalars

Let N=2m+1, d=2m, q=exp(pi i/N), x=q^d and
kappa=q^(d^2/2). The complete-circle node c_m=-2 is SIMPLE.
Its physical summand is the actual intertwiner W:V_N->V_N tensor V_N
of the [central Clebsch theorem](actual_trivalent_steinberg_central_anchor.md),
with genuine dual pi=W^dagger P and pi W=I. Its projector is
E_St=W pi, and

    L_(N,m)=N E_St,   E_St^2=E_St,
    R E_St=omega_m E_St,
    omega_m=kappa (-1)^m q^[m(m+1)], |omega_m|=1.           (1)

Therefore for any original fixed ordered plat or source-certified
matching circuit, its simultaneous endpoint contribution satisfies

    Z_endpoint(epsilon)=omega_m^(sum_i epsilon_i)
                                               Z_endpoint(0), (2)

before the independently specified exterior framing line is restored.
All cups, caps, the original unrestricted marked cut and wire ordering
are unchanged. Equation (2) is just an all-input scalar identity on
each actual endpoint image; it does not use positivity or replace a
structural crossing elsewhere in the diagram.

At even N the last folded node is DOUBLE and L_N is nilpotent there.
Equation (1) must not be copied to that level as a projector identity.
Its actual first-normal source is required, as in the existing even
central black/white calculations.

## 2. The endpoint local saddle roots do not collide

For the raw physical q-Hahn phase in the
[augmented-plat compiler](actual_augmented_plat_phase_compiler.md),
put T=exp(2pi i tau), U=exp(2pi i upsilon), and let Z be the
exponentiated internal summation variable. At the continuum endpoint
xi=j/N->1/2, its Jc=exp(2pi i xi) equals -1. The exact candidate
quadratic from that LEADING phase simplifies to

    [U(T+1)-4T]Z^2+2U(T-1)Z+U(T+1)=0.                     (3)

Its discriminant is

    Delta=16TU(T+1-U).                                    (4)

On the entire real physical domain

    1/2<=tau<=1,   0<=upsilon<=tau,

one has |T+1-U|>=1, hence |Delta|>=16. Indeed, with
phi=2pi tau and psi=2pi upsilon,

    |1+exp(i phi)-exp(i psi)|^2-1
       =4cos(phi/2)[cos(phi/2)-cos(psi-phi/2)]>=0.          (5)

Here cos(phi/2)<=0, while |psi-phi/2|<=phi/2<=pi makes the
second factor nonpositive. The quadratic coefficient also has
modulus at least 4-|T+1|>=2. Thus both roots remain simple; no
division by a vanishing quadratic coefficient or hidden branch
collision occurs on this domain. At tau=1/2 a root can be zero,
so a logarithmic chart there still needs its boundary treatment.

This removes one possible local obstruction. It does NOT select
which root the actual finite q-Hahn sum carries. For an interior
endpoint state with 1/2<tau<1, its internal Fourier derivative still
has argument pi(tau-1/2), strictly between zero and pi/2. Hence the
raw summation does not have a real interior saddle. A complex source
deformation or an exact resummation is still needed.

## 3. An exact N=3 obstruction to positive magnetic leg gauges

Use the ACTUAL endpoint invariant

    Theta=(W tensor I)p,
    Theta_(a,b,c)=N x^-c W_(d-c)(a,b),
    a+b+c=3m,                                            (6)

with the original cup p. The central black vertex is a known
NONZERO scalar times Theta, as proved by its finite quartic transform.
No scalar is inferred here from an unknown graph evaluation.

At N=3, m=1, q=(1+i sqrt(3))/2 and x=q^2. The actual highest vector
is W_0=|0,1>+q|1,0>; its descendants are

    W_r=F_pair W_(r-1)/(1-Q^r),
    F_pair=F tensor I+K^-1 tensor F,
    F|a>=(1-Q^(a+1))|a+1>, K|a>=x Q^-a |a>.

These finite equations and (6) give the six NONZERO entries

| Magnetic triple | Actual Theta entry |
|---|---:|
| (2,1,0) | 3q |
| (1,2,0) | 3 |
| (0,2,1) | -3 |
| (0,1,2) | 3q^2 |
| (1,0,2) | -3 |
| (2,0,1) | 3 |

Consequently

    Theta_210 Theta_021 Theta_102 /
                         (Theta_120 Theta_012 Theta_201)
       =q^-1=(1-i sqrt(3))/2,                             (7)

which is not real.

Under ANY separate nonzero leg gauges

    Theta_abc -> A_a B_b C_c Theta_abc,

the numerator and denominator of (7) contain exactly the same
multiset of labels on EACH leg. Every gauge factor therefore cancels.
A common vertex scalar cancels too. If every nonzero coefficient
could be made positive real, (7) would be positive real, a contradiction.
This obstruction allows arbitrary nonzero complex diagonal gauges,
not just unit phases. Reversing or conjugating the displayed ratio
does not make it real.

Thus the actual central BLACK tensor already prevents the proposed
independent-leg positive normalization. The known endpoint half-twist
scalars in (2) do not change this ratio. No information about the
marked white tensor was suppressed to obtain the obstruction.

## 4. What this does and does not rule out

The actual ordinary white and marked white packets are distinct from
the black tensor and must stay in the complete source. The source-
certified two-vertex contractions have already been resummed to
positive expressions at both parities; those proofs sum additional
indices and retain the original mark. They are fully consistent with
(7), which concerns entrywise magnetic positivity before such sums.

For an arbitrary fixed matching graph or plat, the next step is a
COHERENT resummation of its original contracted endpoint tensors,
or a controlled complex saddle with that source. A full non-diagonal
basis change could also be investigated, but its actual inverse,
exponential norm and transported marked source would need estimates.
Neither the local no-collision statement (4) nor endpoint half-twist
scalarity (2) supplies that global comparison.

In particular (7) does not disprove an arbitrary-plat volume limit,
positivity of a resummed scalar, or a possible geometric period.
It excludes one precise proposed shortcut while retaining the
actual root phases and source normalization.
The displayed counterexample concerns N=3: it rules out an all-level
independent-leg normalization, but by itself does not classify the
larger levels or exclude an asymptotic normalization with a controlled
phase error.

Audit: [original endpoint projectors, six-entry ratio and discriminant](../experiments/audit_actual_central_endpoint_magnetic_phase_obstruction.py).
