# A genuine circle turn changes positive face reflection to full Krein inertia

29 October 2026. The positive original complete-circle face form does
NOT remain positive through the genuine cup/cap quarter-turn used in
the actual four-rung contraction. This is an all-level finite theorem,
including the complete Hermite normals. Its obstruction is already
present on the original cup and its canonical normal direction, not
only on an arbitrary ambient input. An explicit full-rank positive
metric repairs Cauchy at polynomial ordinary source cost; controlling
its energy through overlapping recouplings is a separate problem.

## 1. Exact original operators and the full turned circle

Set N>=2, d=N-1, q=exp(pi i/N), Q=q^2, x=q^d, and

    s_r=product_(k=1)^r 2sin(pi k/N), s_0=1,
    c_j=q^(2j+1)+q^(-2j-1),
    P_N(z)=2T_N(z/2)+2,
    Bhat_v(z)=product_(k=0)^(v-1)(c_k-z)/s_v^2.

Let Omega be the original physical pair Casimir, P the literal
physical swap, and L_N=(-1)^d U_d(Omega/2). The full operator
identities already proved are

    Omega^*P=P Omega, P_N(Omega)=0, P L_N>=0,
    (turn A)_((a,b);(c,e))=x^(a-e)A_((d-a,c);(b,d-e)). (1)

The turn in (1) is the original unscaled cup/cap turn. It is not
a crossing or a relabeling. It is precisely the physical turn used
in the [actual rung/cycle reduction](actual_cube_four_rung_positive_source.md),
and its Newton reversal holds with repeated roots and all normals
in [the full turn theorem](actual_newton_turn_positive_gram.md).

Write M=floor(d/2), k_j=2 for 2j<d and k_j=1 for 2j=d.
Let E_j be the FULL Hermite cluster projector and L_j=L_N E_j.
For v<=j put

    z_j(v)=s_(j+v)/(s_(j-v)s_v^2),
    h_j=sum_(v=0)^j z_j(v)Bhat_v.

The exact all-normal identity is

    turn L_j=N k_j h_j,
    f_N:=turn L_N=N sum_(j=0)^M k_j h_j.           (2)

Here is a parity-independent proof, rather than extrapolation of
the odd rung theorem. The original Frobenius functional satisfies
phi(L_j a)=N Tr(E_j m_a)=N k_j a(c_j). Its multiplication trace
has algebraic multiplicity two on a paired node and one on the odd
simple node; the nilpotent trace is zero only AFTER the full
operator identity is used. Newton duality and genuine turn reversal
therefore give the v-th coefficient of turn L_j as
phi(L_j Bhat_v)=N k_j Bhat_v(c_j). Direct paired-sine factorization
gives Bhat_v(c_j)=z_j(v) for v<=j and zero otherwise. This proves
(2) in the complete N-dimensional algebra, not merely at its nodes.

Consequently, at EVERY distinct Casimir node c_k,

    f_N(c_k)=N sum_j k_j sum_(v<=min(j,k))z_j(v)z_k(v)
                    >=N sum_j k_j=N^2,
    f_N(c_0)=N^2.                                 (3)

All summands are positive real, and z_j(0)=1. The same formula
covers the high partner since c_(d-k)=c_k. In particular f_N is
invertible in the full Hermite algebra, despite the radical of L_N.

## 2. Exact full physical inertia after the actual turn

There is a unique real Hermite polynomial g_N of degree<N whose
positive nodal square roots and paired normal values are

    g_N(c)=sqrt(f_N(c)),
    g_N'(c)=f_N'(c)/(2sqrt(f_N(c))) at a double node. (4)

Every nodal value in (4) is nonzero by (3), so g_N(Omega) is
invertible and g_N(Omega)^2=f_N(Omega). Since the coefficients
of g_N are real, (1) gives the exact congruence

    P f_N(Omega)=g_N(Omega)^* P g_N(Omega).        (5)

It follows, without an eigenvector conditioning estimate, that
the reflected TURNED circle has inertia

    positive: N(N+1)/2, negative: N(N-1)/2, zero:0. (6)

These are the inertia dimensions of the literal swap. Thus no
invertible change of full physical basis, including one mixing all
Hermite channels, can make this turned reflected form positive.
For an explicit negative vector, choose any antisymmetric physical
v and put u=g_N(Omega)^(-1)v; its value in (5) is -||v||^2.

The conclusion concerns the specified physical reflection P. It
does not rule out a different positive metric or a source-dependent
coherent regrouping of a whole graph. In particular it does not
contradict positivity of the actual full cube scalar.

## 3. The obstruction survives on the completed original source packet

Use exactly the original degree-d cup p, ordinary cap ell, marked
row m and canonical Hermite direction t from the
[source frame theorem](actual_tame_c0_hermite_source_frame.md):

    p_u=N x^(u-d), ell_u=x^u/N, m_u=x^(d-u)/N^2,
    ell=p^*P/N^2, ell p=0, ell t=1, mp=1, mt=0,
    (Omega-c_0)p=0, (Omega-c_0)t=theta_N p.

These imply p^*Pp=0 and p^*Pt=N^2. Functional calculus retaining
the actual first normal gives

    [p,t]^* P f_N(Omega)[p,t]
                  =[[0,N^4],[N^4,beta_N]],
    beta_N=t^*P f_N(Omega)t real,
    determinant=-N^8<0.                           (7)

The derivative term f_N'(c_0)theta_N p is present; its contribution
to the upper row is zero because p^*Pp=0. Thus (7) does not omit a
normal. It proves that the complete original two-dimensional source
packet already has one positive and one negative direction after
the turn. One cannot repair this by dropping the cup (which is
null) or by replacing t with a value-only channel.

## 4. A concrete positive Cauchy repair, with exactly polynomial boundaries

The SAME g_N gives a different, positive, full-rank metric

    G_N=g_N(Omega)^*g_N(Omega).                    (8)

This retains every physical degree and Hermite normal. Its definition
uses the actual turned circle, not an unknown knot invariant. Since
g_N(c_0)=N, and ell Omega=c_0 ell, the literal source costs are

    ||p||_(G_N)^2=N^5,
    ||ell||_(G_N^-1)^2=1/N^3.                    (9)

Indeed ||p||_2^2=N^3, ||ell||_2^2=1/N,
g_N(Omega)p=Np, and ell g_N(Omega)^(-1)=ell/N.
For every physical input psi and arbitrary tensor spectators,

    |ell psi|^2 <= N^-3 ||g_N(Omega)psi||_2^2.     (10)

This is an ORDINARY-cap inequality with the actual cup and cap.
It is not a local replacement of the original unrestricted marked
row. Applying it to a marked link first requires its already typed
whole-source conversion, with all original peripheral factors kept.

Equations (5),(8) separate the exact issue at a geometric turn:
the original physical reflection supplies g^*P g, while positive
Cauchy uses g^*g. The latter is a genuine available metric, but
its transport through an overlapping source recoupling is not
controlled by (9). Polynomial correlated cell cost and a positive
closed Racah scalar do not identify these two sewing operations.

Audit: [literal turn, source packet and Hermite square-root checks](../experiments/audit_actual_turned_circle_reflection_inertia.py).
The all-N proof is (2)--(7); complex inertia tests supplement it.
No general graph growth or volume theorem is asserted here.

The positive repair is not identified with a physical mirror.