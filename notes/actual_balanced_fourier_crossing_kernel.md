# A regular balanced full-Psi Fourier kernel for the original crossing source

28 October 2026. At the complete original color, independent finite
Fourier frames turn the entire two-Newton/one-Rogers crossing into a
regular, explicitly normalized full-Psi Fourier kernel. All three
finite source norms vanish on this frame's Fermat multisection.
The resulting operator is EXACTLY the original physical crossing.
The proof first bounds every possible alias error to degree +N,
then eliminates it with one exact ORIGINAL E-coproduct Ward identity.
Consequently all original words, currents, caps and sources are retained.

This is stronger than setting a central scalar to one inside the old
co-source. The external frames and internal Fermat sampling are part
of one specified finite source map. Every intermediate frame change,
original cup/cap, pivot and scalar line remains. The theorem does not
prove a nonzero global geometric intersection or scalar volume limit.

## 1. Original kernel and the finite frames

Use q=exp(pi*i/N), Q=q^2, d=N-1, x=-q^(-1),
s=x^N, so s^2=1. Retain the ORIGINAL common Cartan scalar
kappa. The exact [complete positive layer](actual_trivalent_layer_crossing_source.md)
is the original physical finite block of

    kappa CT_t K(t),
    K=B_N(t/z1,x^(-1)t/z0)
        R_N(z6/z0,x^(-1)z6/t)
        B_N(x^(-1)z7/z6,x^(-2)z7/t).                    (1)

The complete positive Gaussian cell has ALREADY been contracted in
(1); this is its exact finite coefficient identity, not a pointwise
discard of a continuous Gaussian. The finite polynomials are

    B_N(u,v)=sum_(j=0)^d product_(k=0)^(j-1)(u-Q^k v),
    R_N(u,v)=sum_(i+j<N) F_(i+j)/(F_i F_j) u^i v^j.

For nonzero r define the normalized finite frame

    F(r)_(k,a)=N^(-1/2) (r Q^k)^a,
    F(r)^(-1)_(a,k)=N^(-1/2) (r Q^k)^(-a).             (2)

Choose nonzero central values A,B with B!=s A, and fixed roots

    r0^N=A, r1^N=B, r6=x r1, r7=x r0,
    t0^(-N)=r1^(-N)-r7^(-N).                           (3)

The last quantity is nonzero. For each external pair of input/output
Fourier labels evaluate z_i=r_i Q^(label_i), and set t_j=t0 Q^j.
Define the TWO-HEAD Fourier matrix

    M_(k,l;i,j)=kappa/N^3 sum_(m=0)^d K(t0 Q^m),        (4)

at these four external grid points. Define its decoded physical
operator by

    Rhat_+=(F(r6)^(-1) tensor F(r7)^(-1))
                     M (F(r0) tensor F(r1)).            (5)

The factor N^(-3) in (4) is exact: N^(-2) is the two-head
Fourier kernel normalization and N^(-1) is internal root averaging.

**Exact-operator theorem.** Rhat_+=R_+, including its ORIGINAL
Cartan line. Section 2 first proves that their difference can
only have degree +N in the ORIGINAL finite index basis. Section 5
then proves that this difference is zero, using the actual E current.

## 2. The exact degree/carry proof

Expand the three factors of (1) with indices
(i,j),(r,k),(h,l), respectively, each nonnegative pair having sum<N.
A term has external input/output exponents

    a=j+r, b=i, c=r+k-h, e=h+l,
    t-power p=i+j-k-l,
    c+e-a-b=-p.                                        (6)

Consequently

    a in[0,2d], b,e in[0,d], c in[-d,d], p in[-2d,d].

Internal root averaging keeps precisely p=0 and p=-N. Its latter
term is t0^(-N)[t^(-N)]K. For p=-N, the same inequalities show
that a<N and c>=0: a>=N would force output total>=2N, while c<0
would force output total<d. Neither is possible. Thus these terms
already have valid original head indices and change degree by N.

External inverse Fourier extraction folds a,c modulo N. On p=0,
an input a>=N folds to a-N and adds degree N; an output c<0 folds
to c+N and also adds degree N. These two cases cannot coincide:
the former has original input total>=N, the latter original
output total<d. All remaining p=0 terms are exactly the ORIGINAL
physical finite block of (1). This proves the theorem. All root
radius factors are retained in the folding; they are nonzero
scalars and do not alter the degree calculation.

On b physical heads the ideal of strictly positive changes
N,2N,... has b-th power zero. Every original signed crossing
preserves degree. Thus a word in these completed blocks differs
from its original word only by that source-null ideal. The full
original pointed partial trace kills it entrywise, and the pointed
plat source kills it by its actual ordinary-cap constraints.
The marked row alone is not assumed fixed-degree: cups have
total k d, ordinary caps require (k-1)d, and an error would force
the last pair to degree d+N>2d. This is the same proved
[integer-degree source mechanism](actual_crossing_euler_completion_and_weight_source.md).

## 3. ALL three original source norms vanish on this actual grid

Write T=t0^N, and at a grid point put

    u=t/z1, v=x^(-1)t/z0,
    f=x^(-1)z7/z6, r=z6/z0, w=x^(-1)z6/t.

Their central powers are independent of all the finite labels:

    u^N=T/B, v^N=s T/A,
    r^N=s B/A, w^N=B/T,
    f^N=s A/B, (fw)^N=s A/T.

Equation (3) implies exactly

    1-u^N+v^N=0,
    1-r^N-w^N=0,
    1-f^N+(fw)^N=0.                                    (7)

All factors are regular on the stated torus: r^N and w^N are
nonzero and different from one; the same holds for the central
arguments of the Newton full-Psi factors, 1/u and v/u (and
1/f and w). The bare v^N itself need not avoid one. Hence each
original finite polynomial equals
its FULL source-normalized homogeneous term on this multisection:

    B_N(u,v)=S_B(u,v), R_N(r,w)=T_R(r,w),
    B_N(f,fw)=S_B(f,fw).                               (8)

These are consequences of the independently proved finite source
identities and their exact Fermat normalizers, including the
opposite-root Rogers current. No current is thrown away before
the complete sampling map (1)--(5). The regular restrictions in
(3) ensure that the currents in those identities are regular;
at a collision their combined finite expression must instead be
continued, as usual.

## 4. Explicit normalized full-Psi Fourier evaluation

Use the exact notations and constants of
[the complete Fourier source, Sections 5--6 and 11](actual_crossing_shared_face_fourier_source.md).
Let a,b,c,d0 be the retained logarithms of z0,z1,z6,z7,
respectively, X=Log x and tau0=Log t0. Put

    beta=b-a-X, f_log=d0-c-X, rho=c-a,
    z=h+b-tau0, lambda=d0-b+2pi*i.

The original affine 2pi*i mark is retained. Define

    C_boundary=(N^2/phi_N) exp[N(f_log-b)](1-exp(Nrho))
       *Psi_+(beta)Psi_+(h-f_log)/Psi_+(rho)
       *exp{[beta*b-(c-X)(f_log+rho)]/h},

    H_bal=i sqrt(N) phi_N zeta_0 (1-exp(-Nlambda))
                                 exp[(N+z/h)lambda].     (9)

Then EVERY entry of (4) is exactly

    M=kappa/N^3 C_boundary
        *(1-exp[N(c-X-tau0)]) exp(lambda*tau0/h)
        *H_bal*F_ref(lambda).                          (10)

F_ref is the independently normalized full-Phi Fourier function

    F_ref(lambda)=zeta_0/(i sqrt(N))
       *exp[i sqrt(N)lambda c_b-iNlambda^2/(4pi)]
       *Psi_+(lambda+2pi*i+h).                         (11)

Thus (10) has FOUR variable full-Psi factors and its explicitly
known Gaussian and central norm factors. It is an evaluation of
the continued Fourier function with its stated logarithmic marks;
an unrecorded move to a convergent real contour is not asserted.

For the proof, exact shared-face sewing first gives
Psi_-(sigma-h)Psi_+(sigma)=1-exp(Nsigma). After separation the
only internal full function is Psi_+(z-hj). Its orbit is

    sum_j Psi_+(z-hj)exp(lambda*j)
       =Psi_+(z)B_(Q^(-1))(exp lambda,
                                    exp(lambda+z-h)).

Here the second Newton balance is automatic:

    exp(Nlambda)(1-exp(Nz))=1.                         (12)

The fully normalized resonant identity of Section 11 therefore
has zero closure current and equals H_bal F_ref. Substitution
gives (10). Every prefactor and variable full-Psi value in (10)
is finite and nonzero on the regular chart. Alternatively the
finite balanced Newton Fourier recurrence proves directly that
the final orbit sum is nonzero. Hence every entry of this actual
FOUR-LEG Fourier kernel is nonzero.

### A root-independent four-function kernel and its controlled density

All internal-root dependence in (10) cancels. In the same retained
external logarithms set

    G=d0-a-X, R_c=exp(Nrho)=s B/A,
    E=N f_log+(N+1)lambda/2
          +[G(b-c+X)+lambda^2/2]/h.

Then (10) is the particularly simple exact expression

    M=kappa zeta_0^2/N *R_c(1-R_c)^2 exp(E)
         *Psi_+(beta)Psi_+(h-f_log)
            Psi_+(lambda+2pi*i+h)/Psi_+(rho).           (14)

To verify it, the powers in (10)--(11) multiply to
kappa zeta_0^2/N. Balance gives
1-exp(Nrho)=1-R_c, 1-exp(Nsigma)=R_c, and
1-exp(-Nlambda)=1-R_c. In the exponent use
z+tau0=h+b, i sqrt(N)c_b=-(N+1)/2, and
beta+lambda=G+2pi*i. The term (2pi*i b)/h=N b
cancels the -N b from the boundary prefactor. The remaining
exponent is exactly E. No affine mark is removed.

For central A,B in a fixed compact subset of A B(B-s A)!=0,
with fixed bounded root logarithms, the entire density outside
the FOUR full-Psi functions has sharp polynomial size:

    c_K/N <= |kappa zeta_0^2 R_c(1-R_c)^2 exp(E)/N|
                                                       <=C_K/N, (15)

uniformly for EVERY choice of the four finite labels and every N.
Indeed each external logarithm has real part O_K(1/N) and
imaginary part O_K(1). X is purely imaginary. Products in E/h
therefore have bounded real parts, as do N f_log and
(N+1)lambda/2. Also |kappa|=|zeta_0|=1 and R_c,1-R_c are
uniformly bounded above and below. This proves (15).

Thus the reference kernel has an explicit nonzero original-source
local density, with no hidden exponential gauge or periodic
normalizer. Its dilogarithmic action is in its four full functions
and recorded Gaussian. This is a local normalization theorem;
sewing and applying the original global source can still cancel.

### A genuine positive octahedral chart of this ACTUAL kernel

The four classical shapes in (14), with their signed orientations,
are

    u=-z1/z0, v=-z6/z7, w=z7/z1, and -(uvw),

where the last minus denotes its coefficient in the Bloch sum,
not multiplication of its shape by -1. Thus the signed regulator
is D(u)+D(v)+D(w)-D(uvw). On the unit-angle chart let

    0<theta1,theta2,theta3<pi,
    pi<theta1+theta2+theta3<2pi,
    theta4=2pi-theta1-theta2-theta3.

Then u=exp(i theta1), v=exp(i theta2), w=exp(i theta3),
and the negative fourth tetrahedron has positive quad shape
1/(uvw)=exp(i theta4). These are four positive ideal tetrahedra
around an octahedral diagonal, with total angle 2pi.

On every compact subset of this chart, the independently proved
[full-Psi strip estimate](actual_modular_dilog_circle_and_boundary_source.md#a-uniform-geometric-phase-on-the-whole-selected-strip)
and (15) give the actual kernel a nonzero analytic leading density.
Recorded whole-turn shifts contribute their exact nonzero central
factors; they are bounded on the stated central compacta. Its leading
logarithmic modulus obeys the uniform two-sided estimate

    log|M|=N V(theta)/(2pi)-log N+O_K(1),                (15a)

with V equal to the volume of those four positive tetrahedra
and theta the sampled angles in that compact chamber. The O(1/N)
root-modulus and half-step changes alter the logarithm by O_K(1).
This is a statement about the
literal original finite Fourier kernel, not a newly chosen packet.

The volume is strictly concave on this convex angle chamber.
Indeed for L(theta)=D(exp(i theta)),
L''(theta)=-cot(theta/2)/2, and

    Hess V=-diag(cot(theta_i/2))/2
             +cot((theta1+theta2+theta3)/2) 11^t/2.

Both terms are negative definite or negative semidefinite here,
with the first strictly negative. Its unique maximum is
theta1=theta2=theta3=theta4=pi/2, the regular octahedron.
The existence of this local chart does not place the complete
global geometric critical point on its sewn original source.

## 5. An exact ORIGINAL E-current eliminates every possible alias

The degree +N allowance in Section 2 can be removed. Retain the
ORIGINAL complete scaled head current and coproduct

    Ecal|a>=(Q^(-a)-1)|a-1>, Ecal|0>=0,
    K|a>=x Q^(-a)|a>,
    E_total=Ecal_1 K_2+Ecal_2.                          (16)

The actual R_+ commutes with E_total. In the finite Fourier frame,
put (Tf)(z)=f(Qz). Then EXACTLY, for every nonzero frame radius,

    Ecal=z^(-1)(T^(-1)-I), K=x T^(-1).

There is no missing wrap: the coefficient of the input constant
in the first expression is zero, and all other powers lower
without crossing the finite top.

Use z0,z1,z6,z7 for the four grid values, and let M denote (14).
Its exact one-step full-Psi identities give the ratios

    R1=M(z6/Q,z7/Q)/M
       =-z6/z0 *(1-z7/z1)/(1-z6/(Qz0)),
    R2=M(z6,z7/Q)/M
       =q z6/z7 *(1-z7/z1)/(1-Qx z6/z7),
    M(z0 Q,z1 Q)/M=R1,
    R4=M(z0,z1 Q)/M
       =q z1/z0 *(1-z7/z1)/(1-z1/(xz0)).                (17)

All untouched arguments in each ratio are held fixed. Their
denominators are nonzero on the regular central chart. Here
q=-1/x and Q=x^(-2). Substituting (17) proves the rational identity

    x/z6*(R1-R2)+(R2-1)/z7
       =x/z0*(Q^(-1)R1-R4)+(Q^(-1)R4-1)/z1.             (18)

This is precisely the matrix relation E_total,out M=M E_total,in.
The factors Q^(-1) on the right come from transposing the
finite input difference: z_j^(-1) at its shifted row becomes
Q^(-1)z_input^(-1). Thus (18) is the ORIGINAL quantum-group
current, not merely its commuting symbol. Decoding the four
finite frames proves [Rhat_+,E_total]=0.

For completeness, (17) can be checked without an operator claim.
Under logarithmic shifts (delta a,delta b,delta c,delta d0)
=h(Ai,Bi,Ci,Di), put
dl=Di-Bi, dG=Di-Ai, dJ=Bi-Ci. The Gaussian in (14) has ratio

    x^(-dl) exp[dG(b-c+X)+dJ(d0-a-X)+dl lambda]
                          *Q^(dG*dJ+dl^2/2).

Apply Psi(z+h)=Psi(z)/(1-exp z) and its inverse to the four
full functions. For the four shifts in (17) the displayed
ratios result directly. Equation (18) is then an elementary
rational identity; cross-multiplication uses only Qx^2=1.

Finally E_total is INJECTIVE on each physical total-degree
subspace t>=N. Its inputs have first index a=t-d,...,d,
all positive. The first output (t-d-1,d) sees only the
leftmost input, with nonzero coefficient
(Q^(-(t-d))-1)K_d. Remove it and continue: the bidiagonal
matrix forces every remaining input coefficient to vanish.

Let Delta=Rhat_+-R_+. It has degree +N by Section 2 and
commutes with E_total. On input degree zero, E_total Delta=0;
injectivity at degree N implies Delta=0 there. Induct on
input degree j: Delta E_total=0 follows from the preceding
degree, hence E_total Delta=0, and injectivity at j+N
implies Delta=0. At j>=N-1 the target degree exceeds 2d
and Delta already vanishes. This proves Rhat_+=R_+ for
EVERY level, including N=2, composite and even levels.

## 6. Signed words, adapters, source, and scope

The negative block is obtained by the exact complete-color
antiunitary mirror R_-=P overline(R_+)P, with its original
Cartan factor and all frames/marks transported. Applying the
same mirror to (5) gives the EXACT original negative operator.
This does not balance the raw negative continuous Gaussian
at a fixed value of its integration variable; that shortcut
would be false. The literal inverse of (5) is consequently
the original negative crossing as well.

Independent frames at consecutive gates must be joined by their
EXACT finite change of frame. On one shared head it is

    F(r')F(r)^(-1)_(j,k)
       =(1/N)sum_(a=0)^d (r'/r)^a Q^((j-k)a)
       =[1-C]/[N(1-(r'/r)Q^(j-k))], C=(r'/r)^N,        (13)

with its removable finite-sum values. If the central values and
their fixed logarithmic marks stay in a compact nonzero set,
r=exp(Log A/N), these frames and their inverses have uniformly
bounded norms. The same holds for (13). All original cups/caps,
pivots and scalar lines are transformed by those same frames.
Their polynomial norms at the complete color remain polynomial.

No matching of independent central values is required. In fact
forcing direct same-grid closure on a one-component braid drives
this local regular chart to t0=infinity; the adapters in (13)
are what avoid that artificial restriction. Their off-diagonal
tails are generally O(1/N), not exponentially small, and are
part of the retained global gluing and co-source.

After inserting these adapters, decoding the whole finite network
recovers the EXACT original physical word, by Section 5. This
retains arbitrary inserted original currents and coupons when
they are transformed by the same finite frames. The global construction and its
source are recorded in
[the regular balanced word theorem](regular_balanced_fermat_word_source.md).

This theorem resolves the local circle/current normalization by an
actual finite polarization. It supplies a nonzero local Fourier
kernel with the ORIGINAL closed scalar retained. Global selected
geometric survival, source-angle bounds, and dominance still require
control of the sewn finite Fourier sum and the retained adapters.

The [audit](../experiments/audit_actual_balanced_fourier_crossing_kernel.py)
checks independent original crossing matrices, exact finite-index
folding, both signs, full original word/cap sources, the central
balances, and the full-Psi/Fourier scalar at independent complex
grid points.
