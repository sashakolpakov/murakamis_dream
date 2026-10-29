# The original outer color has a squared Fourier kernel

29 October 2026. The full original Hermite source cancels the dangerous
outer-color alias exactly. A finite contour with a SQUARED denominator
then turns a coherent spectral packet into a genuine auxiliary-color
packet, with a strict bound on every complementary physical color.
This is a source identity and estimate, not an identification of a
Casimir coordinate with a meridian.

## 1. Actual color, values, and normals

Let N>=2, d=N-1 and theta_j=(2j-d)pi/N, 0<=j<N. The actual
Casimir nodes are c_j=-2cos(theta_j). Use the literal circle
L_j=(-1)^(j-1)U_(j-1)(Omega/2) and original functional phi from
[the full physical trace theorem](actual_pair_casimir_commutant_and_rotated_trace.md).
For a full Hermite element f set F(theta)=f(-2cos(theta)). For each
ACTUAL auxiliary color N-h, 0<=h<N, that trace gives exactly

    A_N(h)=phi(L_(N-h) f)
      =sum_j [(N-h)cos(h theta_j)F(theta_j)
                              -sin(h theta_j)F'(theta_j)].       (1)

Here the prime is the theta derivative. In particular it retains
the first Casimir normal at every double node. At the odd simple
node theta=0 its contribution is (N-h)F(0), as required.

To derive (1), sin(theta)L_(N-h)(-2cos(theta))=sin((N-h)theta).
The double-node trace is twice (-1)^d times the theta derivative
of that last sine times F. At a node cos(N theta_j)=(-1)^d and
sin(N theta_j)=0. Combining the two equal terms at theta and
-theta gives (1). The simple node is checked by its removable value.
No generic-q derivative is substituted for this fixed-root normal.

An even analytic function F may replace the polynomial on any
symmetric set of nodes if it has the SAME values and theta derivatives
there. Symmetry of those nodes then also gives

    A_N(h)=sum_j exp(i h theta_j)[(N-h)F(theta_j)+i F'(theta_j)]. (2)

## 2. The exact Fourier alias that disappears

Write F(theta)=sum_k Fhat_k exp(i k theta), with Fhat_k=Fhat_(-k).
For a polynomial f the sum is finite. Since

    sum_j exp(i k theta_j)=N(-1)^(d ell) if k=ell N,

(1) gives the exact all-normal formula

    A_N(h)=N^2 sum_(ell in Z)
                   (1-ell)(-1)^(d ell) Fhat_(ell N-h).          (3)

If f has degree less than N, every noncentral possible alias is
killed and

    A_N(h)=N^2 Fhat_h,                  0<=h<N.                  (4)

Thus the physical auxiliary-color vector is precisely the Fourier
coefficient vector of the FULL Hermite representative of f. Reducing
f modulo P_N is allowed here; reducing only its values is not.

Most importantly, ell=1 has coefficient ZERO in (3). For h near N
this would otherwise be the low frequency N-h, with the complete
source growth. The normal term in (1) removes it. This is why an
unweighted node sum is inadequate for the whole-color gap.

For a nonperiodic analytic representative of the same node jets,
one must not assume the separately weighted infinite Fourier aliases
are absolutely summable. The finite contour below avoids this issue.

## 3. A finite residue identity, with its entire boundary retained

Choose a symmetric rectangle [-b_N,b_N]+i[-eta,eta], with vertical
sides halfway between physical theta nodes. Thus

    E(theta)=(-1)^d exp(iN theta)=-exp(-N Im theta)

on either vertical side. Assume F is even and holomorphic on a
neighborhood of the closed rectangle. Put

    K_N(theta)=iN/(E(theta)-1).

Its poles at the enclosed physical nodes have residue one.
Apply residues to (2) and integrate F' by parts around the CLOSED
contour. This is an exact identity:

    sum_(|theta_j|<b_N) exp(i h theta_j)
                       [(N-h)F(theta_j)+iF'(theta_j)]
      =(1/(2pi i))oint exp(i h theta)F(theta)
                            [-iN^2/(E(theta)-1)^2]dtheta.       (5)

Indeed K_N'=N^2 E/(E-1)^2 and N K_N-iK_N'=-iN^2/(E-1)^2.
Equivalently the squared pole has principal part i/(theta-theta_j)^2
+N/(theta-theta_j); its residue is exactly the expression on the
left. Every vertical and horizontal piece of the contour remains.

For 0<=h<=N the oscillatory part of the kernel has these bounds:

* upper side: at most C N^2 exp(-h eta);
* lower side: at most C N^2 exp(-(2N-h)eta);
* vertical sides: at most N^2, because
  exp(-h y)/(1+exp(-Ny))^2<=1 for every real y.

The lower-side frequency is 2N-h, rather than N-h. This is the
finite-contour version of the missing alias in (3).

## 4. A uniform physical-color theorem

Here are explicit sufficient inputs, independent of any knot class.
Let f_N be an actual full Hermite source. Suppose it has an even
holomorphic representative F_N on a fixed rectangle |Re theta|<=2b,
|Im theta|<=eta_0, and constants a,B,gamma>0 such that

    |F_N(u+iv)|<=C N^C exp[N(F0-a u^2+B v^2)].                  (6)

On the enclosed physical nodes require that F_N and its first theta
derivative approximate the ACTUAL f_N node jets with error
poly(N)exp[N(F0-gamma)]. On the complementary physical nodes require
the actual values and first theta derivatives to have the same strict
exponential gap (with possibly another fixed positive gamma).
These are quantitative source assumptions; a principal symbol alone
does not imply them.

Choose halfway endpoints b_N=b+O(1/N). For every fixed delta>0,
there is g_delta>0 such that

    max_(delta N<=h<N)|phi(L_(N-h) f_N)|
                       <=poly(N)exp[N(F0-g_delta)].            (7)

Proof. The approximation and omitted-node errors in (1) cost only
powers of N. In (5) choose a fixed small eta with
B eta^2<min(a b^2/16,delta eta/2,eta/2). For large N, b_N>=b/2.
The upper and lower edges then lose at least delta eta/2 and eta/2
respectively; the vertical edges lose a fixed fraction of a b^2.
There are finitely many edges of bounded length. This proves (7)
uniformly through h=N-1, without an infinite charge-tail argument.

There is also an exact specified analytic corridor interpolation:

    C_N(t)=N^2/(2pi) integral_(-b_N)^(b_N)
                           F_N(theta) exp(iNt theta)dtheta.    (8)

It is even and entire in t. For 0<=h<=delta_0 N, with delta_0
fixed and small,

    |A_N(h)-C_N(h/N)|<=poly(N)exp[N(F0-g)]                 (9)

for a fixed g>0. To see this, on the upper edge of (5) write the
kernel as -iN^2+O(N^2 exp(-N eta)). The constant part, with the
counterclockwise upper-edge orientation, is N^2/(2pi) times the
upper translated integral in (8). Move that integral to the real
segment and retain its two vertical connectors. They are gapped
by (6); the upper remainder and lower side are gapped as above.
The same actual node-jet errors are then added. This proves (9)
for the exact finite integral, before any asymptotic expansion.

The argument is uniform over additional REAL physical parameters
satisfying these source estimates. If F_N is holomorphic and separately
even in their complex continuations, (8) has the same properties.
For that continuation an additional C||Im y||^2 in the exponent is
allowed; (6) with the unchanged F0 is not asserted on a full complex
parameter disk. Shrink this disk so its growth spends less than the
fixed endpoint/current gap before using the complex saddle below.
No analyticity of a merely pointwise error on the physical color
lattice has been assumed.

## 5. The nonzero complex corridor saddle

Suppose additionally on the fixed local rectangle and parameter disk

    F_N(theta,y)=eta_N N^mu b(theta,y) exp[N varphi(theta,y)]
                                                       (1+O(1/N)),

uniformly holomorphically, where b(0,0)!=0, varphi is even in theta
and separately even in y, varphi(0,0)=F0, and

    varphi_theta,theta(0,0)=-D/(2pi), Re D>0.                  (10)

Keep the known nonzero unit eta_N outside C_N. The implicit equation
varphi_theta(theta_*,y)+it=0 has a unique small holomorphic solution.
After shrinking the fixed disks, contour translation within the same
rectangle and the gapped endpoint connectors give

    eta_N^(-1) C_N(t,y)
      =N^(mu+3/2) B(t,y) exp[N Phi(t,y)](1+O(1/N)),
    Phi=varphi(theta_*,y)+it theta_*,
    B=b(theta_*,y)/sqrt(2pi[-varphi_theta,theta(theta_*,y)]).    (11)

The square root continues the convergent Gaussian at t=y=0.
It is nonzero. The local quadratic bound gives an integrable
Gaussian majorant; outside a fixed saddle neighborhood (6) and
the retained connectors give a strict gap. Taylor expansion and
Gaussian moments prove the displayed uniform error. The analytic
O(1/N) source error is bounded on this same contour.

Both Phi and B are separately even. At the complete point,

    Phi(t,0)=F0-pi t^2/D+O(t^4), B(0,0)=b(0,0)/sqrt(D).       (12)

Since Re(1/D)>0, the physical outer-color curvature is strictly
negative. Equations (7)--(12) are exactly the outer source gap and
fixed complex color corridor needed in the general filling theorem.
They do not yet assert that this action is a marked Bloch regulator.

## 6. Application to actual octahedral belt stacks

[The inner physical-color theorem](actual_belt_stack_auxiliary_color_inner_packet.md)
supplies the exact analytic inputs to this result for every fixed
nonempty sign word of n pieces and every fixed outer crossing power a.
Let sigma_i=+1 for a z_(N,h_i) piece and -1 for its typed reflection,
e=sum_i sigma_i, and m=e+a. Its local representative is the actual
product of finite inner packets times

    q^(m d^2/4) exp[iNm theta^2/(4pi)].                       (13)

The literal q^(m d^2/4) is used, not a principal square root.
The original crossing and (13) have the same node values AND
theta normals: partial_theta log R=iN theta/(2pi).
The inner theorem retains exponentially small full-Hermite
replacement errors and the strict angular complement bound.
It also bounds every physical color tuple with an inner color
outside its corridor, for ANY physical outer color.

Consequently the WHOLE (n+1)-color original stack has an exact
separately even complex corridor, a nonzero leading amplitude and
a strict bound on its entire complementary physical color cube.
Writing x_i=h_i/N, its action is

    Phi(x)=n j0-pi x_0^2/[n-i(e+a)]
              +(pi/2)sum_(i=1)^n(-1+i sigma_i)x_i^2+O(||x||^4),
    j0=v8/pi.                                                (14)

Thus in the notation Phi''(0)=2pi i diag(tau_i) of
[the long-filling transfer](general_original_source_long_filling_transfer.md),

    tau_0=i/[n-i(e+a)], tau_i=(sigma_i+i)/2,
    Im tau_i>0.                                              (15)

All analytic source hypotheses of that theorem now hold for these
stacks, at every fixed n>=1. It supplies their nonzero original
long-integral-filling asymptotic with the stated analytic critical
action and original normalization. There is no width threshold in
this source assertion. Width, a and all filling slopes are fixed
before N tends to infinity; both level parities are retained.

The independent geometric requirement is the ACTUAL deformed peripheral
map and absolute regulator comparison for this SAME mixed packet.
Matching (15) to cusp derivatives alone would not prove it. The
[typed global lift](actual_belt_stack_typed_character_composition.md)
now supplies that map, all complete face/collar checks and the absolute
regulator. Combined with the source theorem above, it gives the
[any-subset long-filling volume equality](actual_long_filled_octahedral_belt_stack_volume.md).
The spectral-to-color transform alone is not used to infer that equality.

Independent full proof review rederived the exact alias cancellation,
squared kernel, all boundary bounds, Gaussian normalization and the
joint real/complex parameter quantifiers.
The focused audit checks the polynomial identity with exact arithmetic,
literal physical marked traces over finite fields, and separately
labeled high-precision Gaussian examples. Such examples do not prove
the analytic source hypotheses for an unrelated diagram.
