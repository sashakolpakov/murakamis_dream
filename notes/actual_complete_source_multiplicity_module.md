# Complete source multiplicities with exact original braid and cap data

29 October 2026. The original three-head cup source has a COMPLETE
N-dimensional Hopf multiplicity module, including all intermediate
Casimir Jordan channels. Both original adjacent braids act on this
same module. Its recoupling is an explicit reversed q-Pascal matrix,
not a projection onto the two-dimensional source channel. The actual
cup and ordinary cap become opposite endpoint coordinates after that
recoupling. The original Hermite source packet also has a polynomially
conditioned recoupled frame, although the full recoupling matrix can
have exponential norm.

The same construction reduces the COMPLETE original even plat at
arbitrary fixed width to a central-degree multiplicity space. The full
marked cap is evaluated only after this whole invariant-tensor
identification; its resulting source row and vector have explicitly
polynomial norms. Every reduced signed generator is given below.
No sharp whole-word norm, geometric coefficient, or complete-channel
contractivity is inferred from this exact reduction.

## 1. Original finite modules and conventions

Put N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, x=q^d=-q^(-1),
rho=q-q^(-1), F_a=(Q;Q)_a. On the original balanced V=V_d use

    F|a>=(1-Q^(a+1))|a+1>,
    Ecal|a>=(Q^(-a)-1)|a-1>, K|a>=xQ^(-a)|a>,
    H|a>=(d-2a)|a>, 0<=a<=d.                            (1)

Missing endpoint arrows are zero. The original coproduct is

    F_12=F_1+K_1^(-1)F_2,
    E_12=Ecal_1 K_2+Ecal_2, K_12=K_1K_2.                (2)

Use these iterated coproducts on every physical prefix. All their
N-th E and F powers vanish: the individual terms Q-commute, and the
root q-binomial makes their N-th power the sum of the individual
N-th powers. We retain the unrolled H, not only K=q^H.

The original turns, including all N powers and the pivot, are

    p_(u,v)=N x^(-v) delta_(u+v,d),
    ell_(u,v)=x^(-u)Q^(-u)/N delta_(u+v,d),
    m_(u,v)=x^v/N^2, WITHOUT a degree delta.              (3)

The cup p and ordinary cap ell are literal Hopf maps. They satisfy
the two snake equations, ell p=0 and m p=1. The marked row m is
not an invariant cap and is never replaced by ell. The common
Cartan kappa=q^(d^2/2), original framing, modified dimension and
external scalar chi_N remain on the original crossing/source line.

Write

    Omega=F_tot E_tot+qK_tot+q^(-1)K_tot^(-1).

The original crossing is kappa r_N(Omega_pair), including its
[confluent value AND derivative data](casimir_braiding_and_recoupling_lattice.md).
Its inverse is the literal inverse polynomial. No semisimple root
evaluation is substituted for a double channel.

## 2. A complete three-head Hom space from an explicit highest lift

Let W=(V tensor V)_(integer degree d), with basis
e_j=|j,d-j>, j=0,...,d. For EVERY w in W set

    H_L(w)=sum_(c=0)^d (-xQ)^c E_12^c w/F_c tensor |c>,
    I_w|a>=F_123^a H_L(w)/F_a, 0<=a<=d.                 (4)

Then I_w is an actual unrolled Hopf intertwiner V -> V^tensor3.
Moreover EVERY such intertwiner occurs exactly once. In particular

    Hom_Hopf,H(V,V^tensor3) is isomorphic to W,
    dim Hom=N, dim sum_w image(I_w)=N^2.                (5)

Here is a direct proof including endpoints. A highest vector of
the required weight has integer degree d. If its last-head-c
component is z_c, its E equation gives

    z_(c+1)=-xQ E_12 z_c/(1-Q^(c+1)),

with the action interpreted as in (4). Thus the c=0 component w
determines it and gives exactly H_L. The final c=d equation is
E_12^N w=0. Conversely this proves the E equation for every w.
Its total K and H are precisely the highest K=x,H=d of V.
The quantum-group commutator then gives, along its F string,

    E_tot I_w|a>=(Q^(-a)-1)I_w|a-1>.

The last F arrow is zero by F_tot^N=0. This proves the full
intertwiner, not only a highest-weight kernel comparison.

For each a<N, applying E_tot^a to I_w|a> returns a NONZERO
scalar times H_L(w). Distinct a have different unrolled degrees.
Consequently the N copies of V in (5) are independent. The proof
also gives an inverse: restrict the highest vector to last color0.
No complementary Clebsch channel or internal excursion was dropped.

Both original adjacent signed braids commute with the entire Hopf
action and H. They therefore act exactly on this complete module.
The source cup intertwiner is w=p: E_12 p=0 gives

    H_L(p)=p tensor |0>, I_p(v)=p tensor v.             (6)

The generalized source vector t from the
[tame Hermite theorem](actual_tame_c0_hermite_source_frame.md) must
be lifted as H_L(t). The bare vector t tensor |0> is generally
not highest and must not replace it.

### The total-character slice has no missing generalized extension

The center identity follows directly by multiplying the N shifted
factors FE=Omega-qK-q^(-1)K^(-1):

    T_N(Omega)+K^N+K^(-N)=0,
    T_0=2,T_1=z,T_(n+1)=zT_n-T_(n-1).                 (7)

Indeed product_(r=0)^(N-1)[z-(uQ^r+u^(-1)Q^(-r))]
=T_N(z)-u^N-u^(-N), with u=qK and q^N=-1; F^NE^N=0.
On three heads K_tot^N=(-1)^d. The root Omega=-2 of
T_N(z)+2(-1)^d is SIMPLE, since T_N'(-2)=(-1)^(N-1)N^2.
Thus total-character extensions at -2 are not being silently removed.

In fact ker(Omega_123+2) is exactly the N^2-dimensional image (5).
Any highest vector in it has K=x, hence degree d modulo N. Degree
d is covered by (4). The only other possible physical degree is
2N-1. A highest vector there would have a nonzero F string of
length N, by the same coefficients in (1), ending outside the
available degree range0,...,3d; so it is zero. Applying E repeatedly
to an arbitrary vector in the kernel and using E^N=0 therefore
places it in the strings (4). The intermediate pair Casimirs DO
have their size-two Jordan channels, and all of those remain below.

## 3. Actual complete recoupling is an anti-Pascal matrix

There is a second complete highest chart,

    H_R(w')=sum_(a=0)^d (-1)^a/F_a |a> tensor E_23^a w',

whose inverse is first physical color0. The factor follows directly
from the E equation: on its degree-d slice the K_23 factor at the
next step is Q^(a+1), canceling the Q^(-(a+1)) in Ecal|a+1>.
Define J by H_L(w)=H_R(Jw). Its exact coefficients are

    J_(i,j)=(-xQ)^(d-i)x^j Q^[i(i+1)/2-d(d+1)/2]
                                      [d-j choose i]_Q,
                          i+j<=d; zero otherwise.          (8)

To prove (8), extract physical first color0 from (4). It requires
c=d-i and exactly j first-head lowering arrows in E_12^c.
The q-binomial expansion with E_1K_2 and E_2 gives the displayed
Gaussian coefficient. The remaining exponent simplifies to
i(i+1)/2-d(d+1)/2; no modular half inverse is used. The opposite
antidiagonal is nonzero, so J is invertible. Thus this is a complete
frame change including all colliding intermediate channels.

Put A=Omega_12 restricted to W. It is the literal actual symmetric
tridiagonal degree-d pair Casimir, with explicit entries

    A_(j,j)=q+q^(-1)-q(1-Q^j)^2-q^(-1)(1-Q^(j+1))^2,
    A_(j-1,j)=A_(j,j-1)=-(1-Q^j)^2, 1<=j<=d.

On W the OTHER pair Casimir is

    B e_j=c_j e_j+b_j e_(j-1),
    c_j=q^(2j+1)+q^(-2j-1),
    b_j=Q^j+Q^(-j)-2, 1<=j<=d.                          (9)

Direct extraction in (4) proves (9): only c=0,1 can reach last
color0. Their F_2 E_2 terms cancel exactly; the remaining off
diagonal is b_j. The right-chart calculation similarly gives

    J^(-1) A J=B, J A J^(-1)=B^T.                       (10)

Consequently BOTH complete original signed braid generators are

    R_12=kappa r_N(A),
    R_23=kappa r_N(B)=J^(-1)R_12 J,                     (11)

with their literal inverses for negative signs. The derivative
conditions of r_N at every colliding c_j are essential in (11).
The polynomial has degree<N and supplies the full matrix, not
only its eigenvalues or its two-dimensional source restriction.
Equivalently the entries of f(B) are products of the b_j times
the confluent divided differences f[c_i,...,c_j].

The ordinary tridiagonal A has nonzero adjacent coefficients at
all j=1,...,d. Hence e_d is cyclic for A. Since Jp=Nx^(-d)e_d,
p is cyclic for B on ALL N multiplicities. This establishes
complete source generation by the actual character/Ward algebra.
It is distinct from claiming cyclicity under one braid alone:
at composite levels distinct Casimir nodes can have the same
R eigenvalue, and no reduction based only on those eigenvalues
is authorized.

## 4. Exact original boundary source and a tame Hermite recoupling

The same finite q-binomial identities in (8) give

    Jp=Nx^(-d)e_d, J e_0=p/N,
    ell J^(-1)=(x^d/N)e_0^T.                            (12)

For example row0 of J is x^(-d)(1,x,...,x^d), whereas
ell_j=x^j/N. Thus the cap identity is literal, including its pivot.
For EVERY word W in the two original signed crossings,

    (ell_12 tensor I) W (p_12 tensor I)
          =[ell W_mult p] I_V,
    ell W_mult p=e_0^T [J W_mult J^(-1)] e_d.           (13)

The first equality follows from the actual Hopf intertwiner and
Schur calculation on the explicitly simple V: commuting with H
makes a matrix diagonal and commuting with F makes it scalar.
All actual common Cartan and external framing factors remain.
Any originally prescribed cut functional with value1 on I gives
that same scalar; arbitrary inserted nonintertwining exteriors
must instead retain their literal transported functional.

The original degree-d marked row m and ordinary row ell are
coordinate duals to p,t on their source Hermite plane. Their
full physical use is distinct: for arbitrary w the unrestricted
marked contraction is the matrix

    M(w)_(beta,a)=sum_(u,v) x^v/N^2 [I_w|a>]_(u,v,beta).
                                                               (14)

This matrix, not just m restricted to W, is retained if the actual
exterior asks for a marked row on that pair. No scalar replacement
of (14) is asserted for arbitrary exteriors.

There are useful quantitative bounds BEFORE any ambient recoupling
estimate. Let g_r=F_12^r|0,0>/F_r; every one of its r+1 nonzero
components is the unit phase x^(-second color). The original
Hermite t obeys (A-c_*)t=theta p, theta=(-1)^N rho^2. Since
F_12 is injective in degree d-1, this gives exactly

    E_12^c t=theta N q^(c-1)F_(c-1)/(1-Q^d) g_(d-c),
                                  1<=c<=d.                (15)

The subsequent E coefficients are q(1-Q^j), giving the product
in (15). The distinct last colors in H_L(t) are orthogonal.
Using the finite root reciprocal-square identity therefore gives

    <H_L(p),H_L(t)>=0, ||H_L(p)||^2=N^3,
    ||H_L(t)||^2=||t||^2+N^3|rho|^2(N^2-1)/24,
    N^3/4<=||H_L(t)||^2<=pi^2 N^3/3.                    (16)

Thus the two embedded highest SOURCE columns have condition at
most2 at EVERY N. This concerns those source columns, not all
N multiplicities or arbitrary descendants of t.

The full recoupled source frame is also explicit:

    (Jt)_j=Nx^(-d)(-q)^j(1-Q)/(1-Q^(j+1)), 0<=j<d,
    (Jt)_d=t_0.                                        (17)

Indeed (B^T-c_*)Jt=theta Nx^(-d)e_d; its first coordinate is
fixed by ell t=1 and (12). The recurrence in the remaining
coordinates has ratio -q(1-Q^j)/(1-Q^(j+1)), proving (17).
Its last coordinate follows from the last row of J.

Writing alpha=Nx^(-d), remove the e_d component of Jt. The
remaining vector z is orthogonal to Jp and satisfies exactly

    N^2<=||z||^2=N^2|rho|^2(N^2-1)/12<=pi^2 N^2/3.

The removed scalar is t_0/alpha=(-1)^N rho Hbar, where
Hbar=N^(-1)sum_u sum_(j<=u)(1-Q^j)^(-1). Its absolute value
is at most pi(1+log N). Hence [Jp,Jt] has condition at most
(pi/sqrt(3))[1+pi(1+log N)]^2. This is a proved tame
recoupling of the original two-dimensional source packet into
the complete multiplicity module, not an ambient q-Racah bound.

For arbitrary complete multiplicities there are specified coherent
positive Grams, without a choice depending on the unknown braid:

    G_high=sum_c (E_12^c)^* E_12^c/|F_c|^2,
    G_full=sum_a (F_123^a H_L)^*(F_123^a H_L)/|F_a|^2.   (18)

These give EXACTLY ||H_L(w)||^2 and ||I_w||_HS^2. The right
chart Grams satisfy G_left=J^*G_right J. Formula (18) retains
all mixed copies; it does not claim polynomial conditioning of
the complete Gram or that both braids are contractions in it.
The explicit q-Pascal entries (8) can carry angle energy.

## 4a. A COMPLETE positive Hermite metric with both original sources polynomial

There is a useful non-diagonal Cauchy metric on ALL N channels,
not just the source plane. Use the
[complete physical degree-d Hermite frame](actual_complete_casimir_hermite_packet.md)
V for A: at a double node c=c_j=c_(d-j) take f(c),f'(c),
normalized by f_0(z)=1; at a simple node take f(c). Its entire
inverse is the bilinear Christoffel--Darboux inverse, not a
Hermitian orthogonality assumption. Write nu_j=(-1)^j q^[j(j+1)].
For a double node let Q_j(z)=P_N(z)/(z-c)^2. Its exact block is

    V^T V=K, K_j=sigma_j [[0,1],[1,eta_j]],
    eta_j=r_N'(c)/nu_j+Q_j'(c)/Q_j(c),
    V^(-1)=K^(-1)V^T,
    f_d(c)=x^d nu_j, f_d'(c)=x^d r_N'(c).                (18a)

The single-node formula is V^T V=sigma_j on that block. At
degree d the exact normalizers satisfy

    |sigma_j|=1/|1-Q^(2j+1)|^2  at a double node,
    |sigma_j|=1  at the possible simple node.             (18b)

These follow by the Jacobi continuant CD identity: its endpoint
residue is Q_j(c) f_d(c)/product offdiag, while its next
derivative adds f_d'(c) and Q_j'(c). Thus the inverse and every
normalizer in (18a) are fixed by the original Jacobi matrix;
no selected knot value or favorable metric is used.

The TRUE complete source-multiplicity Racah matrix is

    C=V^(-1) J V.                                        (18c)

This is already restricted to the N-dimensional actual Hom
space. It is not the larger physical adjacent-frame product
before total-character restriction. In RIGHT channel coordinates
z=V^(-1)Jw the complete positive inner product is

    ||w||_ch^2=||V^(-1)Jw||_2^2.                         (18d)

It is full rank, includes every Hermite derivative channel, and
depends only on N and the specified original module. The exact
positive Hermitian matrix is G_N=J^*(V^(-1))^*V^(-1)J. Thus
||p||_(G_N)=||u||_2 and the exact dual norm of ell is ||a||_2;
the bilinear CD matrix K is not itself being called positive.
The exact
generators are D=kappa r_N(Jordan(A)) and C D C^(-1), with
their literal inverses. The first consists of the known unit-value
and polynomial first-jet blocks; the second retains the FULL
coherent Racah transport.

Both original sources in this metric are polynomial. Put
u=V^(-1)Jp and a=ell J^(-1)V. From the exact endpoint source
(12) and CD inverse (18a), their entries at each double node are

    (u_value,u_derivative)
      =(-N nu_j sigma_j^(-1) Q_j'(c)/Q_j(c),
                                      N nu_j sigma_j^(-1)),
    (a_value,a_derivative)=(x^d/N,0).                    (18e)

At a simple node they are u=N nu_j/sigma_j and a=x^d/N.
In particular the original full Cartan phase is retained in the
generator matrices; the source scalar cancellation is exactly (12).

For clarity, the potentially large crossing derivative cancels
in u_value: applying sigma^-1[[-eta,1],[1,0]] to the endpoint
vector x^d(nu_j,r_N') leaves
-x^d nu_j sigma^-1 Q_j'/Q_j in the first entry. This is
an exact SOURCE cancellation; replacing Hermite columns by
independent spectral values would miss it.

There is an exact simplification, stronger than a polynomial
gap estimate. P_N=T_N+2 satisfies the Chebyshev equation

    (4-z^2)P_N''-zP_N'+N^2(P_N-2)=0.

At a double node, this equation and its derivative give

    Q_j(c)=N^2/(4-c^2), Q_j'(c)/Q_j(c)=c/(4-c^2).

The original offdiagonal product of A is (-1)^d N^2, so CD
gives sigma_j=(-1)^d x^d nu_j/(4-c^2). Hence the exact
complete source (18e) is simply

    (u_value,u_derivative)=N(-1)^d x^(-d)(-c,4-c^2),
    (a_value,a_derivative)=(x^d/N,0),                    (18f)

at every double node. At the simple node, present only at odd N,
sigma=x^d nu and u=Nx^(-d), a=x^d/N. All constants and
phases in these formulas are retained.

Thus the source norms are explicit. Put n_distinct=ceil(N/2).
Then

    ||a||_2^2=n_distinct/N^2,
    ||u||_2^2=N^2[sum_double(c^2+(4-c^2)^2)
                                        +1_(N odd)].

The first n_distinct formula here uses the ACTUAL number of
distinct nodes: n_distinct=N/2 at even N and (N+1)/2 at odd N.
The sum is elementary:

    ||u||_2^2=N^2(4N-1),              N odd,
    ||u||_2^2=4N^3,                   N even, N>=6,
    ||u||_2^2=192 at N=4, 64 at N=2.

Indeed the full list c_j=2cos((2j+1)pi/N) has sums
sum c_j^2=2N and sum c_j^4=6N except the resonant levels2,4.
Pairing j with d-j and treating the simple c=-2 separately
gives the displayed formula. Direct substitution proves both
exceptional levels. In particular the UNIFORM source product is

    ||u||_2 ||a||_2<=2N, for EVERY N>=2.                  (18g)

Thus the COMPLETE positive Gram (18d) has polynomial BOTH
original boundary norms, exactly as required for an honest
Cauchy--Schwarz estimate. For every original three-head word,

    |chi_N ell W_mult p|
      <=|chi_N| ||a||_2 ||W_ch u||_2
      <=2|chi_N| N ||W_ch||_op.                          (18h)

One need not replace the source energy by a full operator norm:
with E_N(W)=||W_ch u||_2^2 the stronger pointed bound is

    |chi_N ell W_mult p|^2
       <=|chi_N|^2 n_distinct/N^2 E_N(W).                (18i)

Here E_N is a specified positive doubled energy built from the
actual coherent matrices D,C, the complete initial vector (18f),
and every mixed channel. It is not a sum of independently squared
paths or a new chosen boundary state.

This is a complete source-preserving positive-metric statement,
not a metric pulled back from the unknown word. The subsequent
[exact full-source test](actual_figure_eight_complete_channel_energy.md)
proves that its coherent energy is NONSHARP already for the actual
figure-eight, despite (18g). A single D has polynomial norm, but
coherent transport through C creates the displayed excessive channel.
The [terminal packet Gram](actual_terminal_packet_positive_gram.md)
constructs a different positive metric on this same complete module
with the sharp benchmark rate; general-prefix energy remains unproved.
No individual absolute q-Hahn path or diagonal clock majorant is
substituted for W_ch.

## 4b. A local cap-Ward quotient does not propagate through an adjacent crossing

There is a minimal original-source test for quotienting currents before
taking a positive norm. Set D=A-c_*I on the complete W above. Since
ell D=0, the ordinary-cap row descends to the LINEAR quotient

    Q_cap=W/im D.

This is a state/current quotient, not a quotient of the full observable
algebra. Nevertheless it cannot be propagated unchanged through even
one adjacent original R_23. The exact source-Hermite relation (15) gives

    p=D(t/theta), theta=(-1)^N rho^2!=0,
    [p]=0 in Q_cap.

The primitive has polynomial norm O(N^(7/2)), by the proved tame source
frame and |rho|>=4/N. Thus no large-current asymptotic is needed for
this test. On the other hand the literal original crossing gives

    (R_23 p)_j=kappa p_j F_(d-j),
    ell R_23 p=kappa x^(-d) sum_(r=0)^d Q^(r+1)F_r
              =kappa x^(-d)!=0.                         (18j)

The sum telescopes by Q^(r+1)F_r=F_r-F_(r+1), F_N=0.
Therefore R_23(im D) is not contained in im D, so there is no induced
map R_23:Q_cap->Q_cap. A local quotient would send the original cup
to zero before this crossing and lose the exact unit source (18j).
Equivalently the missing overlap current is explicitly nonzero:

    ell [R_23,A](t/theta)=kappa x^(-d).

All kappas and boundary normalizations are the original ones, and
(13) identifies this pairing with the original whole marked source.
This argument uses one actual source and crossing; it does not rely
on the separate full-observable-algebra no-quotient theorem.

A GLOBAL equation/source quotient can still retain the transported
current and its boundary term. Positive Schur/minimum-energy reduction
is legitimate after those complete compatible variables have been
assembled. The local calculation above supplies no geometric bound
on that global quotient energy. In particular, a polynomial boundary
Riesz norm or a polynomial primitive for one Ward current does not
prove a sharp energy estimate across arbitrary overlapping crossings.

## 5. All odd-head Hom spaces and every even-plat source

The same endpoint argument works at arbitrary fixed width. Put
b=2r+1 and D=r d. Let

    W_r=(V^tensor(2r))_(integer degree D),
    H_r(w)=sum_(c=0)^d (-xQ)^c E_(2r)^c w/F_c tensor |c>,
    I_w|a>=F_b^a H_r(w)/F_a.                            (19)

Then restriction to last color0 proves an exact bijection

    W_r=Hom_Hopf,H(V,V^tensor(2r+1)),
    dim W_r=[z^(rd)](1+z+...+z^d)^(2r).                 (20)

The E recurrence and E_prefix^N=0 prove both directions exactly
as in (4). The highest H and K are d,x, and the complete F string
gives the whole V map. For fixed r>=1 this dimension is
O_r(N^(2r-1)); r=0 means the one-dimensional scalar Hom.
No internal channel between successive braid gates is projected.

Now take an original 2k-head plat, r=k-1, b=2k-1. Define

    Phi_w=(I_w tensor I)p
      =N sum_(a=0)^d x^(a-d) F_b^a H_r(w)/F_a
                                                tensor |d-a>. (21)

These are EXACTLY all invariant tensors in V^tensor(2k).
For a direct inverse expand an invariant tensor by its last head.
Its last-color-d component is highest on the first b heads.
The F equation then determines every other component by

    psi_(d-a-1)=x F_b psi_(d-a)/(1-Q^(a+1)).

This is precisely (21), and the last endpoint holds by F_b^N=0.
Its inverse on w is the coefficient of last TWO colors(0,d)
multiplied by x^d/N. The E equation supplies the same highest
constraint; there is no unperformed normal/source condition.

Both signed original braids preserve these COMPLETE invariant
tensors. Therefore every original plat word has an exact reduced
operator B_word on W_r, computed by (21), the actual physical
word, and that specified coefficient extraction. In particular
this is a strict all-word representation, not the upper corner
of a nonmultiplicative truncation.

Most importantly the FULL original top source is retained. Set

    w_0=p^tensor(k-1), lambda=ell^tensor(k-1) on W_r.

Then Phi_(w0)=p^tensor k, and EXACTLY

    (ell^tensor(k-1) tensor m) Phi_w=lambda(w),
    original plat scalar=chi_N lambda B_word w_0.        (22)

To prove it, compose I_w with the first k-1 ORDINARY caps.
This is a Hopf map V->V and hence scalar. Its highest matrix
entry is lambda(w), because those caps require prefix degree D
and therefore select c=0 in (19). Composing this scalar map
with the LAST literal marked cap on the original cup gives
m p=1. This is a whole invariant-tensor identity. It does not
replace m by an ordinary cap on arbitrary physical sectors.

The reduced source norms in the stated orthonormal W_r basis are

    ||w_0||=N^[3(k-1)/2], ||lambda||=N^[-(k-1)/2],
    ||w_0|| ||lambda||=N^(k-1).                          (23)

Thus no exponential boundary cost is hidden in this complete
all-width reduction. At k=2 these are precisely the source p
and ordinary row ell in (12)--(13). The actual common external
chi_N is unchanged and is not asserted to have polynomial size.

## 6. Every induced generator has an explicit actual Casimir

Write the even prefix in (19) as A_prefix tensor B_head, with
2k-3 and one physical head respectively. On its degree D slice
put

    H_boundary=q x K_B+q^(-1)x^(-1)K_B^(-1)
                         -x E_A F_B K_B,
    O_prefix=F_prefix E_prefix+qK_prefix
                                      +q^(-1)K_prefix^(-1). (24)

The ordering F_B K_B is part of the formula. The full induced
positive braid generators on W_r are

    physical R_i restricted to W_r,       i<=2k-3,
    kappa r_N(H_boundary),                i=2k-2,
    kappa r_N(O_prefix),                  i=2k-1.          (25)

Their negatives are the literal inverses. For k=1 the prefix
is trivial and only the final value r_N(q+q^(-1)) occurs.

Here is an extraction proof, rather than an assumed spectral
matching. For the penultimate pair only last colors0,1 in
(19) contribute to its output color0. The c=0 part gives
xF_B E_B plus the Cartan terms in (24). The c=1 part is
-x F_B(E_A K_B+E_B). The F_BE_B terms cancel, leaving
exactly H_boundary, with no omitted endpoint term. Polynomial
functional calculus then gives the middle formula (25).

For the last pair, its coproduct Casimir can be moved through
the invariant tensor (21) to the complementary even prefix.
This keeps the same Casimir because the actual antipode fixes
it: S(FEcal)=Ecal F, and
Ecal F=FEcal+rho(K-K^(-1)) cancels the shifted Cartan terms.
This is the literal cup duality (3), so no transpose framing
factor or new norm character is inserted. It proves the last
formula (25); specializing the same polynomial gives the full
R, including all Jordan derivatives. Physical generators inside
the prefix commute with its total E/F and give the first formula.

These formulas implement the entire original scalar in a coherent
source-generated module of polynomial dimension at fixed width.
They do NOT establish a sharp bound for products of the two
noncommuting boundary Casimir polynomials. The remaining task is
their complete-channel/coherent angle-energy estimate, with the
source (22), rather than any phase-free path majorant.

## 7. Verification and scope

The finite audit uses the actual signed crossing matrices and their $E,F$ actions. Its scope is the specified word algebra, not an arbitrary coupon algebra; finite checks do not replace the all-level proof.

This is different from the auxiliary classical Clebsch memory in
[the degree-elevation dilation](clebsch_memory_dilation_and_actual_r_excursions.md).
Here we use complete ACTUAL Hopf Hom spaces and invariant tensors,
not a chosen upper subchannel with discarded R excursions. It is
also stronger than retaining only the c_0 Jordan source plane:
all intermediate channels (8)--(11),(24)--(25) are present. Their
nontrivial norms and the geometric global estimate remain open.
