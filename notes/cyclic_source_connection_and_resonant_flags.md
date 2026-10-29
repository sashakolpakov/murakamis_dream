# The cyclic source connection and its resonant flags

Research note, 26 October 2026. The source comparison in
[the Euler calculation](controlled_cyclic_euler_source.md) has an
exact logarithmic connection. Its scalar is another cyclic
dilogarithm, with a specified phase. This gives both its classical
generating action and a regularization at every nontrivial root
of unity. The regularized primitive operator has a computable
kernel. Its source frames still glue by the original actual cap.

These are local identities for the existing cyclic dilogarithm
and actual factorial source. They do not identify the selected
Kashaev period with a geometric cycle. Cyclic Fourier transforms
are already part of the literature coverage recorded in the Euler
note; no novelty is claimed for the underlying cyclic function.
The proofs and the source and cap normalizations here are direct.

## 1. The scalar comparison is an explicit algebraic period

Put q=exp(pi*i/N), Q=q^2, and use a primitive generator X with

    X^N=U, z^N=1-U, z=M^2.

The symbol z in this note is the norm root, not an eigenvalue of
X. The branch near U=0 is initially z=1 and M=1. Let

    S_N(z)=1+z+...+z^(N-1),
    Dcal_N(z)=product_(k=1)^(N-1)(1-Q^k z)^(k/N),
    kappa_N=sqrt(N) exp[pi*i*(N-1)*(N-2)/(12N)].

Define the logarithms in Dcal inside |z|<1 and continue them
together. At z=1 these factors are nonzero, and

    Dcal_N(1)=kappa_N.                              (1.1)

Indeed Arg(1-Q^k)=pi*k/N-pi/2. Pairing k with N-k gives
the modulus sqrt(N), and summing these weighted arguments
gives the displayed phase. This phase is retained at even and
composite levels as well.

For the scalar gamma_N=a_0/S_N of the Euler source comparison,
its exact formula is

    gamma_N(z)=M^(-(N-1)) Dcal_N(z)
                                /[kappa_N S_N(z)]. (1.2)

Here M is the retained square-root meridian mark. To prove
(1.2), start with the previously proved determinant formula

    a_0^N=z^(-N(N-1)/2)
       product_(r=1)^(N-1)[(z-Q^r)/(1-Q^r)]^(N-r).

Replace r by N-k in each numerator and denominator. The
factors -Q^r cancel, leaving Dcal_N(z)^N/kappa_N^N.
Both sides of the resulting root identity are one at z=1.
Continuation from that mark proves (1.2), including its phase.

Thus no unknown scalar is needed for this local comparison.
On its cover it is an evaluation of the specified finite
algebraic product. Its exact connection is

    d log gamma_N=-(N-1)dM/M-d log S_N(z)
            -(1/N)sum_(k=1)^(N-1)
                            k Q^k dz/(1-Q^k z).    (1.3)

This is a rational connection on the marked base. Transport
along a path is the ratio of the explicit products (1.2),
with their branches transported. A loop around z=Q^(-k)
has residue k/N-1 for gamma_N. Resetting an N-th root after
the loop would change that transport.

## 2. The parameter trajectories must be specified

There are three distinct uses of these formulas.

* At fixed primitive center U on a compact marked chart away
  from U=1, z=exp(Log(1-U)/N) approaches one. The earlier
  polynomial coefficient bounds apply.
* At a fixed small primitive coordinate X=x with |x|<1,
  U=x^N approaches zero and z approaches one. This also lies
  in a compact central chart. Bounding coefficients in that
  chart does not by itself bound a contracted complex sum.
* At a fixed norm-root coordinate z with |z|<1,
  U=1-z^N approaches one, and the coherent logarithm is
  N Log z. The compact-chart bound does not apply. Formula
  (1.2) has an exponential, explicitly computable size here.

For |x|>1 the fixed-primitive-coordinate trajectory also
escapes every bounded central chart. A geometric construction
must specify which local polarization and trajectory it uses;
the same letter for two classical-looking shapes cannot do so.

## 3. The generating action with a uniform error bound

For fixed z away from zero and the unit circle set

    G(z)=-log|z|/2-Im Li_2(z)/(2pi),       |z|<1,
    G(z)=-log|z|+Im Li_2(1/z)/(2pi),       |z|>1.

Only dilogarithms inside the unit disk occur in these formulas.
Put w=z in the first case and w=1/z in the second. Then

    log|gamma_N(z)|
      =N G(z)-log N/2+log|z|/2+log|1-z|/2
                    -log|1-w^N|+R_N(z),           (3.1)

where, with delta=abs(|z|-1),

    |R_N(z)| <= [4pi^2 |z|/delta^2+4pi/delta]/(12N). (3.2)

In particular this holds uniformly on compact subsets of
either indicated domain. Here is an elementary proof. Taking
moduli in the determinant formula gives exactly

    log|gamma_N|=-(N-1)log|z|/2-log N/2
       +sum_(r=1)^(N-1)(1-r/N)log|z-Q^r|
                                      -log|S_N(z)|. (3.3)

The denominator product used here has logarithm log N/2 by
pairing r with N-r. For f(t)=(1-t)log|z-exp(2pi*i*t)|,
the composite trapezoid estimate gives

    sum_(r=1)^(N-1) f(r/N)
       =N integral_0^1 f(t)dt-log|1-z|/2+R_N.

Its second derivative is bounded by the numerator of (3.2).
Expanding the convergent logarithmic series in the disk gives

    integral f=-Im Li_2(z)/(2pi),                |z|<1,
    integral f=log|z|/2+Im Li_2(1/z)/(2pi),       |z|>1.

Substitute S_N=(1-z^N)/(1-z) to obtain (3.1).

On the inside chart the real part of the holomorphic generating
action is G, with

    Ghol(z)=-Log z/2-Li_2(z)/(2pi*i),
    dGhol=[-1/2+Log(1-z)/(2pi*i)] dz/z.           (3.4)

This identifies the limiting local connection, rather than
assuming that a root-central normalization has zero rate.

The source-free frame is still an exact expression:

    C_N(z)=M^(N-1) S_N(z) gamma_N(z)
                                  =Dcal_N(z)/kappa_N. (3.5)

Retaining these source factors, the induced regulator norm on
the inverse frame obeys, uniformly on compact punctured subdisks,

    (2pi/N)[-log|C_N(z)|
                 +N log|z| Arg(1-z)/(2pi)]
                      =D_Bloch(z)+O(log N/N).     (3.6)

This follows directly from the already proved
[cyclotomic logarithmic-series estimate](cyclotomic_normalization_tower.md#4-the-local-norm-from-an-exact-logarithmic-series).
The logarithmic correction is part of the regulator metric.
Equation (3.6) is not an equality with the absolute value of
the full knot contraction.

The paired exact identity remains

    gamma_N(M)gamma_N(M^(-1))
             =Gamma_N=M^(N-1)/[N S_N(M^2)]
             =d_N(M)/(N eta_N), eta_N=i^(N+3).    (3.7)

Consequently G(z)+G(1/z)=-abs(log|z|)/2, exactly the
rate of this specified modified-dimension factor. The local
large factors cancel or persist according to the actual cap
and source; they cannot be omitted before contraction.

## 4. A regularized evaluation at every nontrivial N-th root

Let 1<=r<N, zeta=Q^r, and choose M_zeta=exp(pi*i*r/N).
Continue M from one counterclockwise to this mark. Approach
z=t*zeta with 0<t<1 and set u=1-z^N=1-t^N>0. Define

    gamma_tilde_(N,r)=u^(r/N) gamma_N.            (4.1)

On the N-th-root cover this has a finite nonzero value at
z=zeta, with its radial root marked as positive. Exactly,

    gamma_tilde_(N,r)(zeta)
       =M_zeta^(-(N-1)) (Q;Q)_r/N.               (4.2)

For a proof, isolate k_0=N-r in Dcal_N(z). This factor
is (1-Q^(k_0)z)^(1-r/N), while S_N has a simple zero.
Moreover

    (1-Q^(k_0)z)/(1-z^N) -> 1/N.

Reindexing all remaining logarithms gives, with no unspecified
phase on the radial branch,

    product_(k!=k_0)(1-Q^k zeta)^(k/N)
                       =kappa_N N^(-r/N)(Q;Q)_(r-1).

Insert these equations in (1.2); the last factor 1-zeta
completes (Q;Q)_r. This proves (4.2). Thus the singular
scalar is replaced by an explicit algebraic evaluation.

There is more information than its norm. Write the actual
Euler coefficients as

    c_0=1, c_s=product_(j=1)^s Q^(j-1)/(Q^j-1).

Use the full factorial/source reflection

    a_j(z)=gamma_N(z) Q^(-j)(Qz;Q)_(N-1-j).

At the same regularized fiber it gives

    a_tilde_j=0,                                  j<r,
    a_tilde_(r+s)=M_zeta^(-(N+1)) c_s,     0<=s<N-r. (4.3)

Indeed the factorial vanishes precisely in the first case.
At j=r, multiplying (Q;Q)_r by the complementary factorial
gives N, and Q^(-r)=M_zeta^(-2). The subsequent coefficient
recurrence is the original Euler recurrence with index s.

In the primitive regular module, X^N=u and its special fiber
has X^N=0. The whole regularized operator is therefore

    u^(r/N) d_N(X)|_(z=zeta)
       =M_zeta^(-(N+1)) X^r
                        sum_(s=0)^(N-1-r)c_s X^s. (4.4)

Its image is X^r V, its kernel has dimension r, and its rank
is N-r. These images form the standard nested source flag.
In particular this operation is not an invertible change of
primitive operators. Their determinant is u^r before taking
the special fiber. A proposed flow lift must retain this flag
or the corresponding relative lattice, rather than evaluating
an unregularized inverse at the divisor.

There is an exact discrete transport underlying all these fibers.
Keep X and u=1-z^N fixed, and shift z->Qz, M->qM. On the
common marked cover, with epsilon=q^(-(N+1)),

    d_N(X;Qz)=epsilon u^(-1/N) X d_N(X;z).       (4.6)

For a direct proof, the cyclic-product recurrence gives

    gamma_N(Qz)/gamma_N(z)
          =q^(-(N-1)) u^(-1/N)(1-Qz).

Insert it into the exact reflected-factorial coefficients and
use their Euler recurrence. The coefficient of X^0 wraps by
X^N=u and satisfies the same identity. Equivalently, if T_z
denotes the coefficient polynomial with constant term one,

    (1-z) T_(Qz)(X)=Q^(-1) X T_z(X).

Iterating (4.6) from the principal lift z_0=(1-u)^(1/N) gives

    u^(r/N) d_N(X;Q^r z_0)
                    =epsilon^r X^r d_N(X;z_0).   (4.7)

The last factor is an integral unit near u=0. This constructs
the complete local lattice transport, not merely its limiting
rank. After N steps its multiplier is epsilon^N=(-1)^(N-1),
consistent with M->-M on the marked double cover. Dropping
that mark would erase a phase at even levels. The shift here
holds the primitive X fixed; an actual global meridian shift
also changes crossing matrices and Cartan data. This local
equation alone is not the knot's quantum A-polynomial.

The complete integral statement is just as simple. Take
R=C[[u]] and its spectral order S=R[X]/(X^N-u)=C[[X]].
The regularized coefficient a_tilde_j is divisible by u when
j<r, and a_tilde_r is a unit. Consequently its multiplier is

    f_reg=X^r h, h in S^*,
    image(f_reg)=X^r S,
    coker(f_reg)=S/(X^r).                         (4.8)

Indeed replace each lower term u b_j X^j by X^(N+j)b_j
before dividing by X^r. Every resulting exponent is positive,
except the unit constant a_tilde_r. Hence h is a unit.
As an R-module, the cokernel is C^r and is killed by u.
The Smith factors are exactly N-r units and r copies of u;
there are no higher powers. The source comparison is an
isomorphism onto the spectral line lattice X^r S, although
its map into the original R-lattice loses rank. This is an
explicit integral replacement for an invertible-matrix claim.

For a product of m such blocks and integral invertible
adapters, its inverse has poles of order at most m: each
block inverse has at most one pole. Tensoring adds the same
orders. This bound is independent of N for a fixed finite
network. Applying it to a proposed geometric presentation
requires checking that its adapters and scalar source lines
are precisely the regular ones specified here.

For a fixed root zeta=exp(2pi*i*theta), 0<theta<1 rational,
take levels with N theta integral. Equation (4.2) gives

    (2pi/N)log|gamma_tilde_(N,Ntheta)(zeta)|
                              ->-D_Bloch(zeta).   (4.9)

This follows by an integrable logarithmic Riemann sum for
log|(Q;Q)_(Ntheta)|; subtract log N exactly as in (4.2).
For zeta=exp(pi*i/3) it includes all levels divisible by six.
It supplies the local resonant regulator rate, not a knot
volume theorem or a restriction of that conjecture to these
levels.

## 5. The regularized source frames glue by the actual cap

Use the actual dual colors, J^2=Q I, and B=gamma_N J.
Let u=1-z^N be the common local parameter at z=zeta.
The opposite source has residue -(N-r)/N after pullback
under M->M^(-1). On the common cover take

    B_tilde=u^(r/N) B,
    Bdual_tilde=u^((N-r)/N) Bdual.

Both comparison matrices are finite and invertible there.
The second root is transported on the common cover, rather
than independently reset along an inverse radial path. Their
scalar product is, exactly,

    gamma_tilde gamma_dual_tilde
          =u Gamma_N=M^(N-1)(1-z)/N.             (5.1)

For the actual cap C_x^t, x=-M/q, the already audited
dual-frame calculation therefore gives

    Bdual_tilde^(-t) C_x^t B_tilde^(-1)
           =N C_x/[Q M^(N-1)(1-z)]              (5.2)

at the resonant fiber. This is finite and invertible because
zeta!=1. Cups and pivots transform by the same bases.
Thus this local regularization preserves actual duality,
including the Gaussian and modified-dimension factors. It
does not turn the ordinary trace into the modified trace.

The flag pairing also shows why normal data are needed.
The actual C_x is anti-diagonal with nonzero entries. Hence

    (X^r V)^perp=X^(N-r) V                       (5.3)

in the indicated bases. Pairing both leading source vectors
therefore gives zero, even though the cap is invertible and
both vectors are nonzero. This is a local statement about
these factorial source vectors, not about the knot period.

Their full pairing, including its normal factor, is explicit.
Write p_a(z)=(Qz;Q)_a and x=-M/q. Since
C_x e_a=M^a q^(a^2) e_(N-1-a), direct multiplication gives

    p(z^(-1))^t C_x^t p(z)=S_N(z) G_N(M),
    G_N(M)=sum_(a=0)^(N-1)(-1)^a M^(-a)q^(2a^2+a). (5.4)

To prove it, use the exact complement identity

    p_a(z^(-1)) p_(N-1-a)(z)
       =S_N(z)(-1)^a z^(-a)Q^(a(a+1)/2).

The zero of S_N at zeta is simple, and its first normal
coefficient is governed by this finite Gaussian sum. For
example, if N is odd and r is even, M=q^r makes it the
ordinary quadratic sum with b=(N+1-r)/2, and |G_N|^2=N.
Indeed expand its norm, set the index difference to k and
sum Q^(2ka): only k=0 survives. If N is even and r=3 mod 4,
the terms with indices a and a+N/2 cancel, so G_N(q^r)=0.
This follows because their ratio is
(-1)^(N/2+(N+1-r)/2)=-1. Thus even the first normal term
requires its actual phase. These uniform identities locate
the issue in a computable source pairing; they neither show
nor imply vanishing of the full Kashaev invariant.

## 6. What this supplies for the Rivin flow

The [angle flow](rivin_flow_and_quantum_source.md) supplies a
geometric path and its marked A-curve potential. Equations
(1.2)--(1.3) now supply exact local transport for the scalar
source line; (3.1) gives its action along specified trajectories;
(4.3)--(4.4) give its degeneration and source flag; (4.6)--(4.8)
construct its discrete transport on the spectral line lattice;
and (5.2) gives compatible actual gluing through a resonance.

This removes a local scalar and lattice ambiguity. It still
does not assign every geometric shape to the actual network's
norm-root coordinate or transport its selected cut cycle.
In particular a covector can annihilate X^r V. The flag makes
that coupling question explicit, without proving it is nonzero
for the actual knot. Convexity of the classical volume cannot
by itself remove this remaining selected-period question.

[The audit](../experiments/audit_cyclic_source_resonances.py)
checks the new frame identity against independent matrix
determinants, its connection against determinant derivatives,
every resonant source flag and its first-order Smith factors
at the tested levels, the actual regularized caps and their
normal Gaussian moments, the marked complex phase and the proved
error bound. [Results](../experiments/cyclic_source_resonance_results.json).

Reproduce with:

    python3 experiments/audit_cyclic_source_resonances.py
