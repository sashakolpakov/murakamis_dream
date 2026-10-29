# The first quantum-normal connection of an actual root module

Research construction, 27 October 2026. This gives a canonical algebraic
object from the first quantum-normal germ of a specified difference
module. It needs no global differential equation in the quantum
parameter and no off-root horizontal extension of the actual ADO
state. It retains a source and cut, and distinguishes a genuine
connection from the nonsemisimple kernel-to-cokernel case.

This is attached to the specified actual operator, with its pointing.
It is not an identification of its classical geometric component or
of its selected norm with the Bloch regulator. The volume conjecture
remains unproved.

## 1. Root monodromy and its first normal differential

Fix N>=2 and a primitive N-th root zeta. Put

    Q=zeta(1+epsilon), E=C(Y), U=Y^N,
    sigma_Q f(Y)=f(QY), D=Y partial_Y.

Let T(Q)=B(Q,Y)sigma_Q be a specified rank-d difference module,
regular and invertible as a matrix germ over E[[epsilon]]. Write

    H(Q,Y)=B(Q,Y)B(Q,QY)...B(Q,Q^(N-1)Y),
    T(Q)^N=H(Q,Y)sigma_Q^N,
    H=H_0+epsilon H_1+O(epsilon^2).

Because Q^N=(1+epsilon)^N,

    sigma_Q^N=I+N epsilon D+O(epsilon^2).

Thus L(Q)=T(Q)^N-I has the exact first expansion

    L=L_0+epsilon L_1+O(epsilon^2),
    L_0=H_0-I,
    L_1=H_1+N H_0 D.                            (1.1)

The H_1 term differentiates every occurrence of Q in the product,
including its shifted arguments. Omitting those moving-argument
derivatives would give a different object.

Set K=ker L_0, C=coker L_0 and let pi:E^d->C. Both are E-vector
spaces. There is a natural linear map iota:K->C given by inclusion
followed by quotient. Define

    D_N:K -> C,
    D_N(x)=pi(L_1 x)/N^2.                       (1.2)

For f in E it satisfies the Leibniz rule

    D_N(fx)=f D_N(x)+(D f/N)iota(x).             (1.3)

Indeed pi H_0=pi and H_0 x=x on K. In particular for f in C(U),
D f/N=U partial_U f. This is an algebraic differential operator
between K and C with the specified symbol iota; it is not always
an endomorphism of one line.

## 2. Exact cyclic descent

The root operator T_0=B(zeta,Y)sigma_zeta commutes with H_0, so it
preserves K and induces an operator on C. Its N-th power is H_0,
which acts as identity on both spaces. They therefore have cyclic
semilinear descent to C(U).

One direct spanning formula makes the descent explicit. For a vector
x in either space put Av(x)=sum_(j=0)^(N-1)T_0^j x. Then

    x=sum_(r=0)^(N-1) Y^r Av(Y^(-r)x/N).         (2.1)

This follows from the finite Fourier sum
(1/N)sum_r zeta^(-jr)=delta_(j,0). Thus invariants span over E.
Their independence over the invariant field C(U) follows by taking
a shortest E-linear relation, normalizing one coefficient to one,
and subtracting its T_0 translate: all coefficients must be invariant.

The operator (1.2) respects this descent. The exact identity
[T(Q),L(Q)]=0 gives at first order

    T_0 L_1+T_1 L_0=L_0 T_1+L_1 T_0.

On K, after projection to C, the terms with L_0 vanish. Hence
D_N T_0=T_0 D_N. It follows that (1.2) induces

    D_N:K^(T_0) -> C^(T_0)

with symbol U partial_U times the descended iota. This explains
the normalization N^2. Dividing L_1 only by N would leave N times
the natural logarithmic derivation on the central coordinate U.

If eigenvalue one of H_0 is semisimple, then

    E^d=ker(H_0-I) direct-sum im(H_0-I),

and iota is an isomorphism. Its inverse identifies (1.2) with a
genuine logarithmic connection on the descended invariant bundle.
In particular a simple eigenvalue one gives an algebraic line with
connection over C(U).

If there is a Jordan block of size greater than one at eigenvalue
one, iota need not be invertible. One must retain the full K->C
operator. For a rank-two Jordan block it can have zero symbol but
a nonzero order-zero part. Replacing it by an inverse matrix or a
line connection in that case would lose first-normal information.

This construction is initially over the rational function fields
C(Y) and C(U). At a special central fiber, such as U=1, the rank
of H_0-I can jump. Its fiber kernel and cokernel must not be
identified automatically with those generic spaces. Evaluating
the selected period there requires the original saturated lattice
and its source/co-source jets, or the full first-order complex
of Section 4. No complete-fiber regularity is assumed here.

## 3. Gauge invariance, including quantum-normal gauges

Let v=G(Q,Y)w, with G=G_0+epsilon G_1+... regular and invertible.
Then

    B'=G^(-1) B sigma_Q(G),
    H'=G^(-1) H sigma_Q^N(G).

Since sigma_Q^N(G)=G_0+epsilon(G_1+N D G_0)+...,

    H'_0=G_0^(-1)H_0G_0,
    H'_1=G_0^(-1)H_1G_0
       +G_0^(-1)H_0(G_1+N D G_0)
       -G_0^(-1)G_1G_0^(-1)H_0G_0.              (3.1)

Equivalently, as first-order differential operators,

    G_0 L'_1-L_1 G_0=L_0 G_1-G_1 L'_0.          (3.2)

The right side vanishes between K' and C. Thus G_0 identifies
the two kernel-to-cokernel operators canonically. A pure quantum-
normal gauge G_0=I changes H_1 by a commutator with H_0, invisible
between K and C. A Y-dependent G_0 requires the N D G_0 term in
(3.1); it cannot be omitted.

This is gauge invariance of a fixed difference module and its first
quantum-normal germ. Different left multiples of an annihilator
can add extraneous modules. No invariance under such additions is
claimed without their source and cut comparison.

## 4. The exact source and co-source normal equations

Suppose a supplied section has expansion v=v_0+epsilon v_1+... and

    L(Q)v(Q)=epsilon s+O(epsilon^2).

Then

    v_0 in K,
    L_0 v_1+L_1 v_0=s,
    D_N(v_0)=pi(s)/N^2.                         (4.1)

Changing v_1 by h changes s by L_0h and leaves pi(s) unchanged.
Under the gauge of Section 3, s'=G_0^(-1)s. Thus the normal source
class is intrinsic to the specified first-order section problem.

The full first-order source problem is the two-term block operator

    [ L_0  0  ] [v_0] = [0],
    [ L_1 L_0 ] [v_1]   [s].                    (4.2)

Keeping only the map K->C forgets the lift ambiguity and can lose
a normal cut functional. For a supplied scalar cut
p(Q)=ell(Q)v(Q)+k(Q), its first coefficient is

    p_1=ell_0 v_1+ell_1 v_0+k_1.                (4.3)

The transformed data are

    v'_0=G_0^(-1)v_0,
    v'_1=G_0^(-1)v_1-G_0^(-1)G_1G_0^(-1)v_0,
    ell'_0=ell_0G_0,
    ell'_1=ell_1G_0+ell_0G_1,

and (4.3) is unchanged. This retains the normal co-source; an
unpointed connection alone would not recover it.

The full ADO normalization remains the original marked dimension
line d_N(M), including its sign and canceled meridian germ. A chosen
quantum-normal derivative of that line requires its whole lifted
phase and cap data. The construction here does not replace it by
its numerical complete value or infer that derivative from the
root value alone.

## 5. A first-normal source from the original finite lift

There is actual input for (4.1) that does not assume the ADO state
is horizontal off its root. Retain the auxiliary finite lift
G_N(Q,Y) and the pre-specialization annihilator from the
[Q-only finite-sum construction](even_meridian_norm_descent.md):

    Acal(Q,Z,Y,S)G_N(Q,Y)=0 at Z=Q^N,
    P(Q,Y,S)=Acal(Q,1,Y,S)=sum_(j=0)^d a_j S^j.

Choose the coherent Laurent Ore presentation before specializing,
including any fixed shifts needed for nonzero a_0,a_d. It can be
Laurent in S before specialization. At a regular root, G_N is a
whole Q-germ and its value is F_N(Y). Since Q^N=1+N epsilon+...,

    P G_N=-N epsilon
        (partial_Z Acal)(zeta,1,Y,S_zeta)F_N+O(epsilon^2). (5.1)

The moving shifts have already been retained in Acal; their extra
derivatives multiply Q^N-1 and contribute only at second order
to this difference. Define h_1 to be the displayed first coefficient.

Let A(Q,Y) be the solution companion matrix of P, so that for
v=(G_N,S G_N,...,S^(d-1)G_N)^t,

    sigma_Q v=A v+e_d(P G_N/a_d).

Take T=A^(-1)sigma_Q, in the convention of Section 1. Then

    (T-I)v=epsilon r_1+O(epsilon^2),
    r_1=A(zeta,Y)^(-1)e_d h_1/a_d(zeta,Y).        (5.2)

The exact factorization T^N-I=(I+T+...+T^(N-1))(T-I) yields

    s=sum_(j=0)^(N-1)T_0^j r_1.                 (5.3)

Its cokernel class is T_0-invariant, since
T_0s-s=(H_0-I)r_1. Thus the actual first-normal source descends
to C(U), with normalization pi(s)/N^2.

Equations (5.1)--(5.3) construct a source from the central derivative
of the specified finite-sum annihilator. They do not make the actual
root state horizontal for the normal connection. Vanishing of this
source class is a condition to prove, not a consequence of rootwise
T_0-invariance. Its comparison with a geometric regulator source is
still required.

The later [source-corrected construction](source_corrected_quantum_normal_connection.md)
uses this very same preoperator to make the right-hand side a
linear source rule R_N(v), rather than a fixed source value.
Its corrected operator D_N-R_N annihilates every compatible
root section. If the selected section has nonzero symbol iota(v),
this removes all nonconstant central multipliers c(U) while
retaining their actual source derivatives. The unsourced D_N
still need not annihilate the section. The nonzero-symbol
condition and the supplied whole lifting rule are essential.

## 6. A finite-factorial check which distinguishes those statements

Take the local factorial G_N(Q,Y)=(Y;Q)_N. It has the exact central
equation

    Acal=S-(1-ZY)/(1-Y), Z=Q^N.

At Z=1, P=S-I, so T=sigma_Q, H_0=1, H_1=0. The descended normal
connection is U partial_U. The root section is F_N=1-U. It is
T_0-invariant, but it is not horizontal for this connection.

The actual source calculation gives

    h_1=-N Y(1-U)/(1-Y),
    s=-N(1-U)sum_j zeta^jY/(1-zeta^jY)
      =-N^2 U.

Consequently D_N(1-U)=-U=pi(s)/N^2, exactly as (4.1) requires.
This is an explicit source identity from the same finite-factorial
atoms used in the actual knot state. It is not a claim that the
whole knot period is the product of these local sections.

[Exact audit](../experiments/audit_first_quantum_normal_connection.py).
[Results](../experiments/first_quantum_normal_connection_results.json).
