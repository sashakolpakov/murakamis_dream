# A finite actual Frobenius clock graph has the marked Gauss-wall flux

Research proof, 27 October 2026. One actual divided-source clock gives
an algebraic graph in the resolved framing space. Its compact cycle
has exactly the previously computed wall flux, with no limiting
calibration of the constant. A near-identity logarithmic change of
source coordinates relates these finite graphs to the known physical
meridian graph and gives an explicit source-form homotopy.

This identifies a SINGLE inserted Frobenius clock and its cycle.
The old physical head clock changes polarization under the Fourier/
controlled-shift gauge; it is not this inserted position clock by
default. No full word/current or Gaussian comparison is inferred.

## 1. The actual finite clock and its global normal graph

Put c=2pi*i, N>=3, Q=exp(c/N), and r=N in the
[actual high-color source](high_integral_color_frobenius_wall_source.md).
Let R be its block number. Its divided coherent source has

    psi(t)_k=t^k,
    lambda(u)_k=binom(N,k)u^k/(1+tu)^N.

On the source quadric use v=t, a=u/(1+tu), T=va. The binomial
theorem gives the exact actual covariant symbol

    F_N(T)=sigma(Q^(-R))
          =[1+alpha_N T]^N, alpha_N=Q^(-1)-1.           (1)

It is one symbol, not an ordinary power of another clock symbol
substituted for a star product. On the cyclotomic diagonal source,
the inserted head position clock Q^S equals Q^R. Thus (1) is also
the symbol of its inverse inserted head POSITION clock.

On the resolved frame space Y of the
[Gauss-wall calculation](gauss_wall_flux_and_actual_peripheral_character.md),
with north coordinates eta,v,a and south coordinates

    V=1/v, eta'=-v^2 eta, a'=v-v^2a, T'=1-T,
    F=1-eta v=1+eta'V,

define an algebraic source graph i_N by

    eta_N(v,a)=[1-F_N(va)]/v.                           (2)

This quotient is polynomial: its numerator is divisible by v.
The south clock expression is

    F_N^+(T')=[1+(Q-1)T']^N,
    F_N^-(T)=F_N^+(1-T),                               (3)

where F_N^- denotes (1). Equation (3) follows from Q^N=1.
Consequently eta'_N=(F_N^+(Va')-1)/V is also polynomial and
obeys the required transition. Thus i_N is a global algebraic
graph over the source quadric, retaining both compact poles.

At a generic Q, the binomial model instead has the exact factor

    F_N^-(T)=Q^(-N)F_N^+(1-T).                        (4)

The factor in (4) cannot be discarded before taking quantum-normal
jets. Moreover the actual whole divided coherent source has its
own retained normal coefficients; its off-root symbol is not
asserted to be the naive binomial continuation of (1).

## 2. The real compact cycle avoids the wall with bounded clock norm

Let Gamma be the marked real compact source, on which
0<=T<=1 and angular integration of Omega=dv wedge da gives

    integral_(angle) Omega=-c dT.

Along this cycle,

    |1+alpha_N T|^2
       =1-4sin^2(pi/N)T(1-T),
    cos^N(pi/N)<=|F_N(T)|<=1.                         (5)

The lower bound is positive for N>=3. It is uniformly bounded
away from zero as N varies: for example
log cos(pi/N)>=-pi^2/(2N^2 cos^2(pi/3)) gives a fixed positive
lower bound after multiplying by N. In fact the lower bound in
(5) tends to one. Thus Gamma_N=i_N(Gamma) lies in Y minus the
Gauss wall D={F=0}, and this clock and its inverse have no
exponential norm loss on that cycle.

The two source poles lie on the exceptional divisor E, since
F_N(0)=F_N(1)=1. No unmarked identification of their clock
logarithms is made.

## 3. Its marked wall flux is exact at every level

Use the global closed form Xi=dlog F wedge dlog v from the
Gauss-wall theorem. Pulling it back to (2) gives

    i_N^*Xi=-N alpha_N/(1+alpha_N T) Omega.             (6)

For N>=3 the segment 1+alpha_N T avoids zero. Its logarithm,
continued from zero at T=0, has value Log(Q^(-1))=-c/N at T=1.
Therefore

    integral_(Gamma_N) Xi
      =c N Log(Q^(-1))=-c^2=4pi^2.                    (7)

The continuous marked logarithm of F_N is N Log(1+alpha_N T),
which changes by -c even though the two endpoint values of F_N
are both one. This is the full winding, not a point evaluation
which forgets the period. Equation (7) reproduces the marked
physical flux by direct evaluation of the actual finite clock.
It does not alone identify every homology component or the
selected knot's geometric contribution.

The isolated level N=2 has a zero on this straight source segment;
it needs a separately marked relative deformation. Nothing in the
asymptotic argument requires claiming (5) there.

## 4. A whole near-identity source reparametrization

On a common complex neighborhood of the compact source define

    Ttilde_N(T)=-(N/c)Log(1+alpha_N T),
    a_tilde=Ttilde_N(va)/v.                           (8)

The log is the marked one of Section 3. Since alpha_N=-c/N+O(N^-2),
these functions are holomorphic there, extend through v=0, and

    Ttilde_N(0)=0, Ttilde_N(1)=1,
    Ttilde_N'(T)=-N alpha_N/[c(1+alpha_N T)]!=0,
    Ttilde_N(T)=T+O(N^-1)                             (9)

locally uniformly with all fixed derivatives. In the south chart
use Ttilde'_N(T')=(N/c)Log(1+(Q-1)T'), which equals
1-Ttilde_N(1-T'). Thus Phi_N:(v,a)->(v,a_tilde) respects the
actual affine clutch near the entire compact cycle.

The finite clock becomes exactly

    F_N(T)=exp[-c Ttilde_N(T)].                      (10)

Its meridian normal eta_N is therefore the OLD physical meridian
normal evaluated at the reparametrized SOURCE coordinates. In Y
the associated frame coordinate a still differs from a_tilde;
the remaining centralizer translation is explicit, not omitted.
It fixes eta,v and changes a to a_tilde by a->a-eta beta_N, with

    beta_N=[T-Ttilde_N(T)]/[1-F_N(T)].                 (11)

Both endpoints of (11) are removable on the marked cycle. This
is a statement about the resolved framing coordinate, not an
assertion that its translation is the actual internal current.

There is also an exact source-form homotopy:

    Phi_N^*Omega-Omega
          =d[(T-Ttilde_N(T))dlog v].                 (12)

The one-form in (12) extends through both compact poles: its
coefficient vanishes at T=0 and T=1, respectively, and the two
opposite-chart expressions agree. It is O(N^-1) there with
all fixed derivatives. Thus the source area class and its
compact period are retained, including their polar clutch.

## 5. The operator-polarization qualification is essential

Under H_0=G Fourier/N, the OLD head clock is sent to the NEW
head shift V^(-1), while the old head shift is sent to
Q^(-R)Q^S. In particular Q^(-R)Q^S is identity on the selected
diagonal source. The inserted Q^S in Section 1 is not the image
of the old physical head clock under this same gauge.

Consequently (1)--(12) give an explicit actual-clock algebraic
cycle with the correct marked geometric flux, and its regular
logarithmic source reparametrization. Using it as the image of
the knot's original physical cut or its independent internal
centralizer current additionally requires the exact Fourier/
conormal operator dictionary and the full star/current transport.
Matching functions, symplectic forms or winding alone does not
supply that last identification.

The exact operator adapter is derived in
[the controlled Fourier current dictionary](controlled_fourier_current_and_conormal_dictionary.md).
The separate current/polarization and coherent-metric audit is in
[the Fr-clock/internal-centralizer note](frobenius_clock_and_internal_centralizer_map.md).

## 6. Independent coefficient and period checks

[The diagnostic](../experiments/audit_finite_frobenius_clock_graph.py)
constructs the root source from the ACTUAL integral divided matrices,
before testing the binomial clock formula and north/south equality.
Its 72 finite-field cases cover N=3,...,10 and both source poles.
High-precision marked integrals at nine levels N=3,...,256 check
the flux, both removable centralizer endpoints, and the stated
clock-modulus bound. These checks support the uniform proof;
they do not identify the inserted clock with the old physical
head clock.
[Results](../experiments/finite_frobenius_clock_graph_results.json).
