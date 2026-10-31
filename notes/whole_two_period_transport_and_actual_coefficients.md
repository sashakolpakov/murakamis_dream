# A whole two-period transport lattice preserves the actual finite coefficients

Research construction, 27 October 2026. The standard two-nome
product already constructed in the repository defines a flat
rank-one DIFFERENCE object over four independent coordinates.
Its finite first-period transports are exactly the Pochhammer
factors in the original crossing matrices. Consequently every
actual finite word and its original source have a realization in
this whole transport algebra before quantum jets are taken.

This statement concerns transport ratios, not replacement of the
selected knot state by a value or integral of the completed
function. The singular transport lattice, its central norm and
the full peripheral factor are retained. No meromorphic differential
connection at H=0 or selected volume asymptotic is asserted.

## 1. The algebraic difference object precedes any analytic restriction

Work over a characteristic-zero constant field k_0 and put
K=k_0(Q,Qtilde,z,w), with FOUR independent coordinates.
The commuting base automorphisms are

    sigma(z)=Qz, sigma(w)=w,
    tau(z)=z, tau(w)=Qtilde^(-1)w,

and both fix the two nomes. On the free line L=K e define

    sigma_L(e)=(1-z)e, tau_L(e)=(1-w)e.              (1.1)

They commute: sigma(1-w)=1-w and tau(1-z)=1-z. This is the
flat two-period difference presentation. It is a fixed finite-type
rational/birational presentation, not an assertion that its period
section is an algebraic function of the base.

The integral lattice matters. Over
R=k_0[Q^+-1,Qtilde^+-1,z,w], retain R e. This also retains the
z=w=0 source mark and nilpotent jets; its torus localization is
available when needed. The positive
maps in (1.1) are injective semilinear maps over this domain;
their coefficients may vanish on a divisor. Their inverses are
rational maps with the specified poles. One may invert all
translated factors to obtain a genuine Z^2 difference torsor,
but that localization is NOT the original lattice at a zero of
one of those factors. At such a point keep the line, its actual
vanishing transport maps and their normal/source data.

One analytic marked period, on Re H<0, is the existing product

    Q=exp H, Qtilde=exp(4pi^2/H),
    z=exp x, w=exp(2pi i x/H),
    Psi(H,x)=(Qtilde*w;Qtilde)_infinity/(z;Q)_infinity. (1.2)

Both nomes have modulus less than one. Product cancellation gives

    Psi(x+H)=(1-z)Psi(x),
    Psi(x+2pi i)=(1-w)Psi(x).                     (1.3)

The extra Qtilde in the numerator is essential for the second
equation. In the
[two-nome atom note](unfolded_atom_cyclotomic_divisors_and_two_nome_source.md)
our w is its y, and its numerator argument is Qtilde*y.
That note supplies and marks (1.2) by exact products. Nothing
here derives a unique completion from the first Ward equation.

## 2. Every finite transport is the original finite product

Define t_n(z) by sigma_L^n(e)=t_n(z)e, first over K. Direct
iteration gives for EVERY integer n

    t_n(z)=product_(j=0)^(n-1)(1-Q^j z), n>=0,
    t_(-n)(z)=1/product_(j=1)^n(1-Q^(-j)z), n>0.    (2.1)

They satisfy the exact cocycle identity

    t_(m+n)(z)=t_m(z)t_n(Q^m z).                   (2.2)

For any nonzero marked period of (1.1), in a domain where its
values are defined meromorphically,

    Psi(H,x+nH)/Psi(H,x)=t_n(exp x).               (2.3)

The right side gives the rational continuation of the RATIO,
even when neither individual period has a root value. A sigma-
periodic completion factor cancels in (2.3) exactly.

In particular

    (z;Q)_n=t_n(z), (Q;Q)_n=t_n(Q),
    {a choose k}_Q=t_a(Q)/[t_k(Q)t_(a-k)(Q)].       (2.4)

These are identities of whole finite products before evaluation.
The physical q with Q=q^2 and the original half-Cartan root
characters are retained on their specified covers when actual
coefficients are pulled back; the new notation does not erase them.
For instance the actual balanced positive crossing is, with its
original unwrapped support and full Cartan line retained,

    r_+=(-1)^k x_1^(-b-2k)x_2^(-a+k)
           Q^(ab+(a-b)k-k(k+1)/2)
           {b+k choose k}_Q t_k(Qx_1^2 Q^(-a)),

and the negative one is

    r_-=x_1^b x_2^(a-k)Q^(-ab)
           {a+k choose k}_Q t_k(Qx_2^2 Q^(-b)).     (2.5)

Their derivation, original Cartan factors and exact cups/caps are
in [the actual crossing calculation](figure_eight_whole_source_identity.md),
Section 2. Here (2.4) realizes every factor in (2.5) by the
universal period transport. It does not omit their common scalar.

## 3. Universal finite-word preservation, with the actual lattice

Take the original finite coefficient array at fixed level, with
all actual crossing coefficients, cup/cap factors, pivots, framing
and meridian lifts, cut row and full modified dimension. Replace
each finite Pochhammer by (2.1), and each Gaussian by (2.4), on
its specified support. Keep every monomial, phase and original
normalization factor unchanged.

The resulting transport word equals the original coefficient as
a whole rational function in its actual q/M variables and clock
characters. Its value is independent of the extra two-period
completion: each local first-period ratio already descends from
the four-coordinate period object to Q,z.

This equality is preserved by finite products, sums, matrix
contractions and literal insertion of all actual index moments.
It therefore gives EXACTLY the original finite state, including
its source and every whole normal derivative. This is a uniform
finite-word identity for arbitrary braids/cups/plats; it does not
assume a triangulation move or a new state integral identity.

At a singular factor evaluate the CANCELLED WHOLE coefficient
in the original lattice. Do not evaluate the numerator and
denominator period separately. The ordinary actual root support
has factorial denominators of length below N, hence those factors
are nonzero there. A vanishing norm or a supplied source ratio
may require the original relative/normal lattice instead.

For example the actual finite Ward gauge is

    f_N(z)=sum_(j=0)^(N-1) z^j/t_j(Q_N).

Its EXACT affine source is

    f_N(Q_N z)-(1-z)f_N(z)=z^N/N.                  (3.1)

Indeed adjacent coefficients cancel and t_(N-1)(Q_N)=N.
The nonzero source must not be replaced by a homogeneous cyclic
equation. Nor does the transport equality mean that f_N itself
is the scalar function Psi_N; the latter has additional central
period/source data, explicitly computed in the atom note.

The new conclusion compared with
[rational-state folding](rational_period_pushforward.md) is this
actual finite-word preservation and singular-lattice statement.
The two-nome definitions and their rational-point factorization
are already part of the repository and established literature.

## 4. Commensurate periods keep the cyclic norm as central transport

At the marked physical H_N=2pi i/N the analytic power restriction is

    Q=Q_N, Qtilde=1, w=z^N.                       (4.1)

The two periods obey NH_N=2pi i. On the base sigma^N and tau
are both identity after (4.1), but their LINE maps are

    sigma_L^N(e)=t_N(z)e=(1-z^N)e=tau_L(e).        (4.2)

The equality t_N=1-z^N uses primitiveness, with no primality or
odd-level assumption. It is NOT sigma_L^N=I. The nontrivial
central tau transport is exactly the finite cyclic source norm.
Off the divisor 1-z^N=0, the commensurability loop
sigma_L^N tau_L^(-1) is trivial, as it must be.

If nu^N=1-z^N with the original mark nu=1 at z=0, the normalized
small-step transport (1-z)/nu has cyclic norm one. This is the
finite Kummer/Hilbert-90 part. It is obtained only after adjoining
nu and inverting its zero divisor. At z^N=1, the original
transport in (4.2) is noninvertible, while the normalized map
requires division by zero. The original line lattice and its
vanishing/normal source must remain; the norm-one gauge is not
a regular replacement there.

## 5. The original peripheral norm and its whole quantum adapter

The full original peripheral factor is

    d_N(M)=epsilon_N (M-M^(-1))/(M^N-M^(-N))
          =epsilon_N M^(N-1)(1-M^2)/(1-M^(2N)).     (5.1)

Keep epsilon_N and any specified whole phase lift exactly. At the
root, (4.2) identifies its denominator with t_N(M^2). Thus its
central norm is a transport factor of the same object, including
all factors such as 1+M^n on their actual marked substitutions.
No such factor is replaced by its numerical complete-point value.

There is a necessary WHOLE qualification. The actual fixed-N
power coordinate W=M^(2N) is independent before restriction.
Under the actual half-meridian step M->qM it obeys

    W -> Q^N W,

whereas the independent dual-nome coordinate w in (1.1) is fixed
by sigma. The two markings agree at (4.1); they are not an
off-root equivariant identification. The actual source and its
q/M power-graph derivatives must therefore be retained.

In particular the alternative first-period norm lift

    d_N^tr(Q,M)=epsilon_N M^(N-1)t_1(M^2)/t_N(M^2)

agrees with (5.1) at Q_N but is generally DIFFERENT as a whole
q-germ. Their exact ratio is

    C_N(Q,M)=d_N^tr/d_N=(1-M^(2N))/(M^2;Q)_N.      (5.2)

The whole regular continuation near M=1 is obtained by canceling
their common 1-M^2 factor before evaluation. At a generic regular
M and Q=Q_N,

    D_Q log C_N=sum_(j=0)^(N-1)
                       j M^2 Q_N^j/(1-M^2 Q_N^j).  (5.3)

For N=2 this is already visible:

    d_2=epsilon_2 M/(1+M^2),
    d_2^tr=epsilon_2 M/(1-QM^2).

Their values agree at Q=-1, but (5.3) at M=1 is -1/2.
The phase lift cancels from this comparison if it is the SAME
actual lift on both sides. Thus replacing the original peripheral
denominator by a cyclic Pochhammer before differentiating loses
an actual normal source term.

More generally the cancelled whole function at M=1 is
C_N=N/product_(j=1)^(N-1)(1-Q^j). Since
Re[Q_N^j/(1-Q_N^j)]=-1/2 for 1<=j<N, its actual physical-root
normal satisfies

    Re[D_Q log C_N]_(Q_N,M=1)=-N(N-1)/4.           (5.4)

Thus an adapter whose root value is exactly one can still have
quadratically growing quantum-normal data. This does not change
its root value; it explains why that value cannot replace its
whole marked source in a quantum-jet comparison.

One may record (5.1) in the universal TWO-period base as the
formal transport ratio epsilon_N M^(N-1)(1-z)/(1-w), with
z=M^2 and w=W. This records its whole rational source factor;
it does not identify its fixed-N power-graph dynamics with the
analytic modular restriction away from the root. Alternatively
keep (5.1) separately, which is what finite-word preservation in
Section 3 does. Either way, no original factor has been changed.

## 6. Fixed-n exceptional slopes are compatible, but not a global blowup

The atom note proves independently, for n FIXED, Q=zeta_n exp(eps)
in a closed negative-real eps sector and U=exp(t n eps),

    F(Q,zU)/F(Q,z) -> (1-z^n)^t,                  (6.1)

with its logarithm marked from z=0, uniformly on |z|<=r<1 and
compact t sets. The resonant terms m=kn in the exact logarithm
give -t z^(kn)/k; nonresonant terms vanish. Exponential bounds
and a slightly larger r<1 give the stated uniform remainder.

For t=a/b the EXACT telescope uses shifted arguments,

    product_(j=0)^(b-1) R(Q,zU^j,U)=F(Q,zU^b)/F(Q,z).

On U^b=Q^(an) its root value is (1-z^n)^a, and the marked
individual exceptional period has nu^b=(1-z^n)^a. It is NOT
the assertion R^b equals that finite product away from the
exceptional restriction. Nor is (6.1) a regular holomorphic
extension across an entire complex blowup neighborhood, where
other cyclotomic divisors still accumulate. No n-growing limit
is interchanged with this fixed-n statement.

This local exceptional/source result, the whole difference
presentation and the actual finite transport identities fit one
period object. They do not prove that its analytic completion
preserves the selected global knot contraction. The latter still
requires its original period/cycle, all internal projectors and
the source/co-source comparison, rather than only equal nilpotent
jets or equal cyclic norms.

Exact transport/source audits: [script](../experiments/audit_whole_two_period_transport.py)
and [results](../experiments/whole_two_period_transport_results.json).
The argument and the cancelled peripheral-normal adapter have a
separate [independent proof audit](whole_two_period_transport_independent_audit.md).
