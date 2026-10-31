# Adaptive resonant sampling of the actual source and the raw-quotient obstruction

28 October 2026. There is a constructive EXACT adaptive Fermat sampling
which puts the complete original finite source on the resonant divisor;
Section 5 proves it entrywise for either crossing sign. This is a genuine
base change before the original finite windows. It evades, rather than
contradicts, the fixed-scalar raw-quotient obstruction proved first below.
No arbitrary exterior coupon, renormalized invariant, or generic
oscillatory countermodel is involved. Other original Newton/Rogers
currents remain compulsory after this sampling.

## 1. The closure character is invisible to the complete finite crossing

Keep the ports and complete signed Laurent kernels of
[the actual trivalent crossing](actual_trivalent_layer_crossing_source.md).
Inputs are z0,z1 and outputs are z6,z7. Put d=N-1. For fixed t0!=0,
independent of the head variables, the character in
[the exact resonant Fourier source](actual_crossing_shared_face_fourier_source.md#11-an-exact-resonant-fourier-source-including-its-closure-current)
is

    A=(z7/z1)^N-(z7/t0)^N,
    D=1-A.                                           (1)

For the positive crossing it is exactly
exp(N lambda)(1-exp(N z)), with the retained marks
lambda=Logz7-Logz1+2pi*i and z=h+Logz1-Logt0.
Equation (1) is a Laurent polynomial, so its monodromy notation does not
introduce an additional choice here.

Let K_sigma(t) be the COMPLETE raw signed kernel, including all finite
Newton/Rogers factors and the original shared negative Gaussian when
sigma=-. Let Pi_phys extract the original finite input/output block.
Then, identically before taking the t constant term,

    Pi_phys[A K_sigma(t)]=0,
    Pi_phys[D K_sigma(t)]=Pi_phys[K_sigma(t)].         (2)

This also holds after the exact finite root-orbit average, for every N,
every original color, and either crossing sign.

The proof is the actual finite output support. In the positive layer the
last Newton factor is

    B_N(x^(-1)z7/z6,x^(-2)z7/t),

and in the negative layer the last Rogers factor is

    R_N(g_- z7/t,x^(-1)z7/z6).

Every monomial in either has second-output exponent e between 0 and d;
none of the other factors contains z7. Both monomials of A contain
z7^N. They therefore force second-output exponent at least N, which the
original finite output window excludes. The first monomial also raises
the required second input by N, but that additional exclusion is not
needed. Gaussian integration changes coefficients and cannot change
these exponents. The same proof works term by term on any fixed scalar
root orbit. This proves (2) without assuming that the meromorphic
homogeneous/current pieces separately have finite support.

More generally Pi_phys[A^k K_sigma]=0 for every k>=1. If a polynomial
f(A) is inserted directly on this complete local kernel, its finite
physical projection is f(0) times that of the uninserted kernel.

## 2. This is an exact statement for the whole original knot source

Apply (2) at any physical crossing of an actual signed word, retaining
all original input/output barriers, pivots, markings, and framing.
The physical local operator is unchanged if it is multiplied by D.
Consequently its contraction with the original source is unchanged.
This applies to nonzero hyperbolic-knot periods as well as to general
words; for example the independently proved original figure-eight
source is

    K_N(4_1)=sum_(n=0)^d |(Q;Q)_n|^2>0.              (3)

Thus there is no exact raw restriction of this original source to A=1
which retains the COMPLETE inserted crossing and its D-inserted source
pairing: restriction would send D K_sigma to zero, whereas its original
pairing is the nonzero quantity (3).

This does NOT authorize the opposite algebra quotient A=0. Equation
(2) is a statement about a specified finite projection of a specified
complete kernel. The finite projection is not multiplicative on the
Laurent algebra: A has a factor z7^N, while multiplication first by
z7^(-N) can return those exponents to the physical output window.
An arbitrary later operator/coupon need not retain (2). Accordingly the
precise assertion is the actual insertion-functional identity (2), not
an algebraic support statement for the whole coupon algebra.

Nor can (2) be applied separately to the meromorphic S/I sectors. Those
sectors are not finite Laurent kernels; their continued high Fourier
modes are exactly what restore the original finite source in their sum.

## 3. What the orbit and deck equations do determine

The root-orbit map proves equality of the COMPLETE original sourced
functional with its finite-orbit version. The only unwanted orbit alias
has positive integer degree N, and the original closure kills every
nonempty alias selection. Invariance under changing the fixed scalar
t0 is therefore exact. These are consequences of the original finite
degree/source data; they are not new constraints forcing A=1.

Likewise the local exact formula

    T_N=H_N F_ref+Psi_+(z)(1-A) I_-

has a completely normalized, nonzero reference coefficient H_N on the
regular part of A=1. Its compulsory current restores the source away
from that divisor. Equation (2) shows why one cannot obtain the original
global geometric coefficient by setting that current to zero through a
raw multiplicative restriction of the complete source.

Beyond the adaptive map in Section 5, the wanted additional structure is
a SOURCE map to an action-normalized
geometric vanishing-cycle/formal block, including the finite window and
its currents. One must calculate the image of the actual marked class
there and show that its coefficient is nonzero with subexponential
normalization. This would be a genuinely derived or microlocal source
comparison; its local resonant residue cannot simply be substituted for
the complete finite pointing.

## 4. Exactly what compact divisor rigidity would and would not prove

If two meromorphic sections of the same line on a connected compact
normal variety have the SAME complete divisor, their ratio is a nowhere
zero global holomorphic function, hence constant. One exact nonzero
value fixes that constant. This is a valid rigidity principle.

Its present application is missing two pieces of actual data: a globally
defined geometric component with its full divisor, and the map of the
original source/cosource to that component. Known local homogeneous
divisors and total deck invariance do not supply either piece. The
complete section includes currents with different divisors and different
continued homogeneous components. Even uniqueness of the COMPLETE
exact section would not by itself compute its decomposition into
action-normalized geometric periods.

The obstruction (2) is stronger than an abstract caution: the original
finite pointing already pairs nontrivially with the closure defect
which raw resonant restriction would erase. Therefore a successful
global compact-torsor rigidity argument must explicitly transport that
pointing, rather than infer its balanced support from the fixed-scalar
orbit map. The following adaptive construction does transport it to a
balanced sampling of the COMPLETE finite kernel.

## 5. A constructive adaptive Fermat sampling evades the obstruction

Define a head-dependent orbit radius by the algebraic equation

    t0^(-N)=c(z1,z7):=z1^(-N)-z7^(-N).               (4)

On c!=0 choose any of its N roots and sample the COMPLETE raw kernel on
the orbit t=t0 Q^j. The finite sum is independent of that root choice.
Since K_sigma(t) has t exponents in [-2d,d], its average is exactly

    CT_t K_sigma+c(z1,z7) C_sigma,
    C_sigma=[t^(-N)]K_sigma.                         (5)

Now apply the original physical windows. Every monomial of C_sigma has
incoming second exponent -b with b>=0 and outgoing second exponent e
with 0<=e<=d. The first term z1^(-N)C_sigma in (5) requires incoming
second index b+N>=N, and the second term z7^(-N)C_sigma has outgoing
second exponent e-N<0. Both are excluded. Therefore, ENTRYWISE,

    Pi_phys [(1/N)sum_(j=0)^d K_sigma(t0 Q^j)]
                           =Pi_phys CT_t K_sigma.    (6)

This is true at either sign and every original color, with the same
continuous Gaussian retained for a negative crossing. It consequently
preserves every original whole-word source, without needing a global
degree argument to cancel residual local aliases. Its scalar and all
finite barriers are unchanged.

By (4), the actual character (1) is identically A=1 on this algebraic
sampling. Thus the local resonant Fourier comparison has its exact
reference coefficient H_N and no additional closure current. This
closes a source-balancing step which a fixed scalar orbit did not close.
The construction does not erase the OTHER original B/R current sectors
created before that one-function comparison.
An additional balanced external Fourier-frame completion can remove
those local currents too. Its degree proof must be performed before the
original whole source is applied; it is not a consequence of (6) alone.
That construction is now proved in the
[local balanced Fourier theorem](actual_balanced_fourier_crossing_kernel.md)
and the [whole-word source theorem](regular_balanced_fermat_word_source.md).
It uses independent regular local grids and retains the exact rational
Fourier adapters. The remaining geometric source problem concerns that
explicit sewn network, rather than an unidentified local normalizer.

At c=0 an individual sampled radius tends to infinity. The COMPLETE
finite average nevertheless has the explicit Laurent-polynomial
extension (5), and its physical projection has the extension (6).
Separated homogeneous/current expressions require their matched joint
continuation there; one cannot infer separate finite limits from (5).

There is no contradiction with (2): substituting (4) before projection
changes the head dependence of the moment variables. It is not an
A-linear restriction of the fixed-scalar inserted source. Algebraic
base change and the physical projection do not commute. This is the
precise mechanism by which the adaptive source map evades the no-go.

## 6. The remaining adaptive local norms form a two-generator boundary ideal

There is a concrete algebraic target for that additional transport at
complete color. Write

    a=z0^N, b=z1^N, c=z6^N, d=z7^N,
    s=x^N, s^2=1, T=t0^N=bd/(d-b).

On the regular torus, the first Newton, final Newton, and middle Rogers
norms in the original positive layer are, respectively,

    D_first=T[1/(s a)-1/d],
    D_B=d[1/b-1/(s c)],
    D_R=1-c/a-c/(s T)
        =-(s c/T)D_first-(c/(s d))D_B.               (7)

The last equality uses only 1/T=1/b-1/d and s^2=1. Thus the THREE
norms generate exactly the two boundary-exchange relations
d-s a and b-s c after localization at the displayed nonzero coordinates.
They vanish jointly precisely when

    c=s b, d=s a.                                   (8)

Keep the source-selected decompositions
B0=S0+D_first I0, R=T_R+D_R J, Bf=Sf+D_B If, with all logarithmic marks.
Their complete scalar kernel obeys the exact aggregate identity

    B0 R Bf-S0 T_R Sf
      =D_first[I0 R Bf-(s c/T)S0 J Bf]
       +D_B[S0 T_R If-(c/(s d))S0 J Bf].             (9)

It follows by expanding in the stated order and then substituting (7).
This reduces the remaining local current transport to TWO specified
boundary relations, rather than three unrelated local normalizers.
It does not assert that the raw finite projection annihilates each
meromorphic term of (9). Regular balanced external sampling can impose
(8) before the finite projection, and must retain its Fourier changes
of frame when the local blocks are sewn.

[The audit](../experiments/audit_actual_orbit_closure_source_obstruction.py)
checks the full raw signed finite layers, the actual physical R matrices,
nonzero discarded terms, finite-orbit aliases, and original pivotal
whole-word source identities. The grading/output-support proof above is
uniform in N.
