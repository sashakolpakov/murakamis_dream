# The whole meridian profile and its regular period are equivalent

Research proof, 27 October 2026. The canonical actual polar
subtraction gives a uniform comparison of the whole scaled
meridian function and its regular period, including every fixed
resonance center. The original full-state monomial supplies an
even resonance factor exactly. Uniform division across its zeros
is justified by a fixed boundary norm, not by pointwise division
or a jet argument.

The result is conditional only on the explicitly stated domination
of the polynomial-size ordinary-color tail when normalized by
the Kashaev value. It does not assert that this growth or a whole
profile limit exists for a general hyperbolic knot. It also keeps
the fixed-root meridian normal distinct from the moving-q
integral-color normal.

## 1. Exact actual functions and the tail assumption used here

Use the actual functions of
[the regularized Kashaev period](regularized_kashaev_period.md):

    q_N=exp(pi*i/N), Q_N=q_N^2, Y=M^2,
    K_N=F_N(1), S_N(Y)=1+Y+...+Y^(N-1),
    F_N(Y)=S_N(Y)R_N(Y)+P_N(Y).                 (1)

Here P_N is the unique polynomial of degree at most N-2 with
`P_N(Q_N^j)=C_j(q_N)`, 1<=j<N, and R_N is Laurent polynomial.
The ordinary-color theorem gives

    |C_j(q_N)|<=D_N, D_N<= (N/2)^(b-1),
    |[Y^r]P_N|<=2D_N, 0<=r<=N-2.               (2)

Work along any sequence with K_N nonzero and

    epsilon_N=N D_N/|K_N| ->0.                 (3)

A positive exponential lower bound for |K_N| implies (3), but
is stronger than needed here. Put c=2pi*i and use the entire
scaled meridian coordinate

    M_N(z)=exp(z/(2N)), Y_N(z)=exp(z/N), U=Y_N(z)^N=exp(z).

Define

    g_N(z)=F_N(Y_N(z))/K_N,
    pi_N(z)=P_N(Y_N(z))/K_N,
    r_N(z)=N R_N(Y_N(z))/K_N,
    rho_N(z)=M_N(z)^(N-1) r_N(z).              (4)

All these functions are entire in z. The retained monomial in
rho_N is the original full-state normalization, not a newly
chosen gauge.

For any compact K in the z-plane and every nonnegative integer l,
the coefficient formula (2) gives the direct bound

    sup_K |partial_z^l pi_N|
       <=2(N-1)D_N exp(max(0,sup_K Re z))/|K_N|.             (5)

Indeed each differentiated exponential contributes `(r/N)^l`,
of modulus at most one. Thus the complete interpolation tail
and all its fixed jets vanish locally uniformly under (3).
No growing Vandermonde inverse or unproved q-normal estimate
is involved.

## 2. The original full-state factor gives an exact even resonance function

The symmetric geometric sum gives exactly

    H_N(z)=S_N(Y_N(z))/[N M_N(z)^(N-1)]
          =sinh(z/2)/[N sinh(z/(2N))].          (6)

At apparent common zeros this is its entire continuation. It
is even and H_N(0)=1. Hence (1) becomes the exact whole identity

    g_N=H_N rho_N+pi_N.                        (7)

The uncentered geometric sum would instead tend to `(exp(z)-1)/z`.
Its additional factor `exp(z/2)` is accounted for by the exact
monomial in (4). Removing or ignoring that factor would give
the wrong Weyl transformation for the regular coefficient.

Put

    H(z)=2sinh(z/2)/z, H(0)=1.

On every fixed disk, for all sufficiently large N,

    H_N(z)=H(z)B_N(z),
    B_N(z)=[z/(2N)]/sinh(z/(2N)),
    B_N=1+O_K(N^(-2)).                        (8)

B_N is a holomorphic nonvanishing unit on that disk. Its poles
are at the distant points cN times nonzero integers. Thus (8)
is locally uniform, including all fixed zeros of H. Those zeros
are exactly `z_k=ck`, nonzero integers k; they are simple. For
N>|k| they are exact zeros of H_N as well.

The full modified dimension from the actual state is

    d_N(M)=eta_N (M-M^(-1))/(M^N-M^(-N)), eta_N=i^(N+3).

Therefore its complete Weyl-even scaled cocycle is exactly

    N d_N(M_N(z))/eta_N=1/H_N(z).              (9)

This retains both the actual phase eta_N and every finite root
divisor. It is a whole meromorphic identity, not just its value
at z=0. In particular the full normalized ADO profile is

    N calN_N(M_N(z))/(eta_N K_N)
            =g_N/H_N=rho_N+pi_N/H_N.           (10)

The last summand must be subtracted before claiming holomorphic
uniformity at a resonance. A small nonzero residue still gives
a pole. For example C_1=1 forces a nonzero pole at z=c at every
finite level, even if its normalized residue tends to zero.

There is also an exact actual half-source interpretation. The
marked rational Weyl splitting beta_N from
[the source Weyl-gluing theorem](twisted_cotangent_source_and_weyl_gluing.md)
satisfies

    beta_N(M)beta_N(M^(-1))=c_N(M)^(-1),
    c_N(M)=N M^(N-1)/S_N(M^2).

Thus, at this scaled meridian, without any limit or growth
assumption,

    c_N(M_N(z))=H_N(z)^(-1),
    beta_N(M_N(z))beta_N(M_N(-z))=H_N(z).       (10a)

The odd/even-level phase and its unpaired even-level factor
remain the original ones in beta_N. Hence the resonance factor
is already the exact norm of the actual marked half-source,
not an externally imposed entire function.

### 2.1 It is also the character of the original finite compact source

On the actual N-dimensional source let J e_j=j e_j and n=N-1.
Then exactly

    H_N(z)=(1/N)Tr exp[z(J-n/2)/N].             (10b)

This is the finite sum (6), with its original 1/N. The compact
coherent symbol is explicitly

    exp[-nz/(2N)] [1+(exp(z/N)-1)T]^n.

Its original compact-source period is (10b), by the proved
coherent trace formula. Uniformly for z in compact sets and
0<=T<=1 this symbol tends to `exp[z(T-1/2)]`. Consequently

    H(z)=integral_0^1 exp[z(T-1/2)]dT.          (10c)

Thus the resonance factor is at once an actual source character,
the exact Weyl norm (10a), and the inverse full peripheral
cocycle (9). No index theorem or identification of different
quantum theories is needed for these equalities.

## 3. Uniform division is valid through every resonance center

Choose radii 0<r<R with R not equal to 2pi times a positive
integer. Let

    m_R=min_(|z|=R)|H(z)|>0.

For all sufficiently large N, (8) gives
`min_(|z|=R)|H_N(z)|>=m_R/2`. Whenever u_N/H_N has its
holomorphic continuation to the disk of radius R, the maximum
principle gives the fixed division bound

    ||u_N/H_N||_(|z|<=r)
                     <=(2/m_R)||u_N||_(|z|=R). (11)

There is no loss of control at an interior resonance. Its
removable quotient is holomorphic before applying the maximum
principle. For our exact numerator `u_N=g_N-pi_N`, this condition
holds because (7) supplies the entire quotient rho_N.

This proves the following equivalence under (3):

* g_N converges locally uniformly on C to a holomorphic g;
* rho_N converges locally uniformly on C to a holomorphic rho.

The same proof is local on any open domain, using finitely many
small boundaries avoiding its resonance zeros. The limits are
necessarily related by

    g=H rho, g(0)=rho(0)=1.                    (12)

For the nontrivial implication, at each fixed z_k the exact
numerator vanishes for all large N. Equations (5) and local
uniform convergence give g(z_k)=0, so g/H has a holomorphic
removable continuation. Put rho=g/H. The numerator of

    rho_N-rho=(g_N-g-pi_N-(H_N-H)rho)/H_N

is exactly divisible. Equations (5), (8), and (11) prove local
uniform convergence, including all resonance centers. They also
give the explicit estimate

    ||rho_N-rho||_(D_r)
      <=(2/m_R)[||g_N-g||_(boundary D_R)
              +||pi_N||_(boundary D_R)
              +||H_N-H||_(boundary D_R)||rho||_(boundary D_R)]. (13)

The forward implication follows directly from (7). The same
norms show that local boundedness of the two families is
equivalent. In particular the regularization neither manufactures
nor loses an unspecified normal-family assumption.

At the centers the removable value can be recorded explicitly:

    rho_N(z_k)=[g_N'(z_k)-pi_N'(z_k)]/H_N'(z_k),
    H_N'(z_k)=(-1)^k/[2iN sin(pi k/N)],
    H'(z_k)=(-1)^k/(ck).                       (14)

Thus fixed resonance derivatives and the regular quotient obey
the same convergence. Higher derivatives follow either from
Cauchy's formula after (13) or by repeated division.

## 4. Weyl symmetry and the regular coefficient

The actual [Weyl theorem](actual_weyl_descent.md) gives
`F_N(Y^(-1))=F_N(Y)`, hence g_N is exactly even. H_N is even as
well. Equation (7) implies

    H_N(z)[rho_N(z)-rho_N(-z)]=pi_N(-z)-pi_N(z).

The numerator is exactly divisible. Applying (11) and (5)
proves, even without convergence of rho_N,

    rho_N(z)-rho_N(-z) ->0 locally uniformly.   (15)

Every profile rho in (12) is therefore even. It may still be
algebraic: the example `rho=1, g=H` satisfies all these resonance,
Weyl and normalization constraints. If rho is entire and algebraic
over C(z), it is an even polynomial; these identities do not
exclude such a regular coefficient. The required whole period
factor is already nonalgebraic and supplies all the resonance
zeros.

By contrast the uncentered limit r satisfies
`r(-z)=exp(z)r(z)`. A nonzero global r with this property cannot
itself be algebraic. This is a normalization issue resolved by
the original full-state monomial, not an obstruction to an
algebraic centered coefficient.

Also `rho_N(0)=N R_N(1)/K_N=1-P_N(1)/K_N ->1`. Thus R_N(1)
is nonzero for all large N on the sequence (3), and using the
intrinsic normalization

    M_N(z)^(N-1)R_N(Y_N(z))/R_N(1)

gives the same local-uniform limits and the same equivalence.
No division by an unproved nonzero period is made before (3).

## 5. Fixed-root and integral-color normal maps have the same U but different sources

Compare the preceding path with the actual integral-color one

    qfrak_N(z)=exp(c/(2N)+z/(2N^2)),
    M=-qfrak_N(z)^N=exp(z/(2N)),
    Qfrak_N(z)^N=exp(z/N)=Y_N(z).              (16)

Thus M, Y and U=exp(z) agree exactly. The quantum parameter does
not: q is fixed at q_N in (1)--(15), while it varies in (16).
On the actual common module put

    delta=1-Q^N, w=M Q^(-N)-M^(-1).

The two source paths are exactly

    fixed root: delta=0, w=M-M^(-1),
    integral color: delta=1-Y_N(z), w=0.        (17)

They are different legs of the two-wall geometry. The head-word
excursion factor delta*w vanishes on both legs, but that does
not identify their derivatives, pivots or selected contractions.

The actual ordinary integral pivot/twist differs from the frozen
root auxiliary source by the already computed route factor

    qfrak_N(z)^(Nn kappa_D)
           (Qfrak_N(z)^N)^(sum_closed j_a),
    kappa_D=writhe-b+1, n=N-1.

Knot parity removes only its root value. In this normal coordinate
the remaining whole insertion is

    exp{z[n kappa_D/(2N)+(sum_closed j_a)/N]}.   (18)

Its modulus and every fixed z derivative are bounded on compact
z sets uniformly in N, since `0<=sum_closed j_a<=(b-1)n`.
It remains a nonconstant source insertion. A bound on its
individual weights does not control cancellations in a selected
sum, so it cannot be deleted when comparing normalized profiles.

There is also a q-normal contribution. For a specified auxiliary
finite-word lift, the path derivative in (16) contains
`q partial_q/(2N^2)` in addition to the fixed-root contribution
`M partial_M/(2N)`, together with the actual source derivatives
from (18). Neither (2) nor the polar bound (5) bounds that
q-normal derivative of the selected quantum word.

The integral-color sampling centers are accordingly different:

    z_(N,k)=-ckN/(N+k) ->-ck,
    C_N(qfrak_N(z_(N,k)))=C_k(q_(N+k)).         (19)

These are moving q-color resonances, whereas the fixed-root
zeros in (14) are exactly ck at every sufficiently large level.
Equations (16)--(19) specify the coordinate and source adapter
needed for a comparison; they do not assert equality of the two
selected profile functions.

## 6. Exact scope

The tail bound, full-state cocycle, quotient norm and equivalence
of whole/regular profile convergence are exact consequences of
the actual regularized state. They hold through the resonance
centers, and retain the marked monomial and full modified
dimension.

The independent
[whole Gamma source comparison](whole_gamma_frame_profile.md)
proves an actual function-level refinement, with no K_N growth
assumption. If z=ca and

    Phi_a(T)=G(T)^(-a)/Gamma(1-a),
    G(T)=(exp(cT)-1)/c,

its actual middle-index q-normal residual V_(N,L)(a) and the
marked meridian half-source obey

    N^(-a)beta_N(M_N(ca)) ->Phi_(-a)(1/2),
    V_(N,L)(a)=u_N(a) beta_N(M_N(-c b)),
    b=a/(1+a/N), u_N(0)=1, u_N=1+O_K(1/N).     (21)

The unit is specified by nonvanishing J-products there and
remains valid through resonance zeros. The reparametrization
b aligns their finite moving and fixed zeros; it cannot be
omitted in a unit comparison. Consequently

    Phi_a(T)Phi_(-a)(T)=H(ca).

Thus (10a), (10b) and (21) match actual source functions and their
norm, not only a formally similar entire function. These are
scalar source-line comparisons. They do not identify the full
selected knot modules, their regular period coefficients or
the state profiles in (16). In particular the opposite and
slightly reparametrized half-source coordinate in (21) is not
the identical-M normal path used in (16).

No positive volume growth, whole normal-family convergence,
algebraicity of the regular coefficient, or equality of q-normal
and meridian-normal sourced periods has been proved here.

## 7. Audit

[audit_scaled_meridian_regular_profile.py](../experiments/audit_scaled_meridian_regular_profile.py)
and its
[results](../experiments/scaled_meridian_regular_profile_results.json)
check the finite centered character, both marked half-source
norms and full cocycle at 85-digit precision, including odd and
even N=2 through 18. They check the interpolation coefficient
and derivative bound for bounded nodal data, and removable
quotient values at the exact positive and negative resonances.

The quotient stress family is an explicitly declared universal
Laurent-polynomial family satisfying the same interpolation
divisibility; it is not asserted to be a knot invariant. The
general-knot analytic proof is (5)--(14). A separate compact
grid through N=128 checks the improved centered factor rate
O(N^(-2)); no general-knot growth assumption is inferred from
these audits.
