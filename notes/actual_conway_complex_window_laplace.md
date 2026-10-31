# A uniform complex packet for the actual positive Conway core

29 October 2026. A fixed rectangular window about the unique strict
complete optimizer gives an EXACT separately-even holomorphic packet
for the original positive auxiliary-color core. Its complex asymptotic
has a nonzero analytic amplitude at every level parity. The proof keeps
the finite lattice window, its endpoint currents and all nonzero
cotangent modes. It is not an inference from a real-grid asymptotic.

This note concerns the core packet and its comparison with the WHOLE
positive core on real physical colors. Signed alias estimates and a
geometric peripheral interpretation are additional inputs; they are
not supplied by the complex Laplace argument itself.

## 1. The actual lattice and a fixed strict window

Fix one retained cylindrical robust Conway factor. Expand its seed
blocks into h leaves and products, and let H be its number of leaves.
The expanded expression tree has H-1 products. Delete only the final
forced-flat product, whose exact multiplication coefficient is one,
and impose its exact input relation i+j=D, where D=N-1.

The remaining H leaves and H-2 products have a unique strict complete
optimizer by the existing boundary-barrier theorem. Every leaf index
lies strictly between zero and D/2, and every retained product's four
strict inequalities hold there.

There are exactly

    d=2H-3                                                     (1)

free integer wire coordinates. Indeed the H leaf outputs and H-1
product outputs give 2H-1 variables before the final closure. Turn
outputs are eliminated one at a time by r_out=D-r_in. Fixing the root
output and its final input-sum relation removes two variables. The
last relation involves variables of disjoint child subtrees with
coefficients +1 or -1, so one can solve it integrally. There is no
parity-dependent lattice index or omitted congruence class.

Choose the remaining physical wire indices k_1,...,k_d as coordinates
and put x=k/N. Every other physical wire has the exact form

    r_w=N ell_w(x)+delta_w,                        (2)

where ell_w is integral affine and delta_w is a fixed integer. The
constants delta_w retain every occurrence of D=N-1. They are not
silently replaced by zero. Let x_0 be the strict complete optimizer
in these coordinates. Choose a sufficiently small closed rectangular
box B centered at x_0, entirely inside the strict source domain.

Let chi_l=h_l/N be the auxiliary-color deficit of leaf l. At physical
colors h_l>=0, its exact positive core coefficient is

    A_(N,r_l)(h_l)=N^2 s_(2r_l)
              /[s_(r_l)^2 s_(r_l-h_l)s_(r_l+h_l)].              (3)

On a small fixed complex chi polydisk, replace every sine factorial
in the SAME leaf and product weight by the
[canonical marked interpolation](exact_factorial_interpolation_and_complex_contours.md)
G_N. Define the packet

    Z_N^win(chi)=sum_(k in Z^d, k/N in B) I_N(k/N,chi),           (4)

where I_N is the product of the H interpolated factors (3) and the
H-2 actual interpolated Newton multiplication coefficients.

After shrinking B and the chi polydisk, every scaled factorial argument
has real part in a fixed compact subinterval of (0,1), on a fixed
complex thickening of B. Thus I_N is holomorphic and nonzero there.
For large N, EVERY lattice point in (4) is an actual admissible core
state at every physical color in the chosen real chi window. No
support indicator changes inside this box. Formula (4) is finite and
separately even in every chi_l, by the two factors r_l+-h_l in (3).

## 2. Exact normalization of the interpolated summand

Write every factorial argument as N alpha_nu(x,chi)+c_nu, with
integer c_nu, and let sigma_nu be its signed multiplicity. The
canonical uniform expansion gives

    G_N(N alpha+c)
       =sqrt(2N sin(pi alpha)) exp[N J(alpha)]
          (2sin(pi alpha))^c [1+O(N^-1)],
    J(alpha)=integral_0^alpha Log(2sin(pi u))du.                  (5)

Its marks are continued from positive real arguments. The remainder
and its fixed derivatives are uniform on smaller complex compact
sets. Equation (5) follows directly from the canonical expansion
at alpha+c/N; its shift factor is ESSENTIAL when c is nonzero.

Define

    f(x,chi)=sum_nu sigma_nu J(alpha_nu(x,chi)),
    b(x,chi)=2^(3-3H) product_nu
        sin(pi alpha_nu)^(sigma_nu/2)
        (2sin(pi alpha_nu))^(sigma_nu c_nu).                     (6)

All square roots and powers are continued from the positive real
complete window. A leaf has one numerator and four denominator
factorials, with its extra N^2. A retained product has two numerator
and five denominator factorials. Consequently

    sum_nu sigma_nu=-3H-3(H-2)=6-6H,
    I_N(x,chi)=N^(3-H) b(x,chi) exp[Nf(x,chi)]
                                      [1+O(N^-1)].             (7)

The leading amplitude b is nonzero and positive on the real complete
window. It contains all D=N-1 offset factors from (2); there is no
unknown periodic normalization. At chi=0, f is exactly the complete
source action V_E/pi in the selected free wire coordinates.
For general chi it is the sum of the actual product actions and

    g_chi(x_l)=J(2x_l)-2J(x_l)
                            -J(x_l-chi_l)-J(x_l+chi_l)          (8)

over the leaves. Here x_l=ell_l(x) is its limiting leaf coordinate.

## 3. A finite-window complex lattice Laplace lemma

The following elementary argument applies to (7), and more generally
to a fixed-dimensional analytic summand N^a b_N exp(N f), provided:

* f is holomorphic on a fixed complex thickening of B and a parameter
  polydisk, real on the real slice at zero;
* at zero it has its unique strict nondegenerate maximum x_0 in B,
  with negative definite real Hessian;
* b_N=b+O(N^-1) uniformly holomorphically, with b(x_0,0)>0;
* the source sum uses the entire rectangular integer lattice window.

Shrink the box if necessary so the real Hessian stays uniformly
negative definite throughout it. The implicit-function theorem gives
one holomorphic critical point x_*(chi) near x_0. Put

    phi(chi)=f(x_*(chi),chi),
    A(chi)=-f_xx(x_*(chi),chi).

Then uniformly on a fixed smaller complex parameter polydisk,

    sum_(k/N in B) N^a b_N(k/N,chi) exp[Nf(k/N,chi)]
       =N^(a+d/2) (2pi)^(d/2)
          b(x_*(chi),chi)/sqrt(det A(chi))
                     exp[Nphi(chi)] [1+O(N^-1)].               (9)

The determinant square root is positive at zero. Here is a proof
that explicitly controls the discrete nonzero modes.

For each coordinate enclose its retained integer interval by a
rectangle whose vertical sides are halfway between consecutive
lattice points, and whose horizontal sides have fixed imaginary
heights +-eta. The endpoints differ from B's endpoints by O(1/N).
The product residue formula with kernels pi N cot(pi N z_j) is
EXACTLY the original finite sum. On a vertical half-grid side
|cot(pi N z_j)|<=1. On a horizontal side,

    cot(pi N(x+i eta))=-i+O(exp(-2pi N eta)),
    cot(pi N(x-i eta))= i+O(exp(-2pi N eta)).                    (10)

At parameter zero the real part of f changes by O(d eta^2) under
these imaginary shifts, because its first derivatives are real.
The same bound holds with a small additional parameter error after
shrinking the parameter disk. The real boundary of B has a fixed
strict gap below f(x_0,0).

Choose eta first, small enough that O(d eta^2)<pi eta and small
enough to retain half the boundary gap. Then choose the fixed
parameter disk sufficiently small to retain both inequalities,
relative to Re phi(chi). Every contour piece with a vertical side
is exponentially below the critical value. Every nonconstant
cotangent-error term in the product expansion has at least the
factor exp(-2pi N eta); the possible phase increase is smaller
than exp(pi N eta). Polynomial prefactors cannot remove these
strict exponential gaps.

The 2^d constant horizontal kernel terms have coefficient N^d/2^d
and the same orientation. Deforming their horizontal boxes to the
real box only adds vertical connectors with the already established
boundary gap. Thus the exact sum equals N^d times the ordinary
analytic integral over B, up to a uniform exponentially smaller
error. Replacing the real half-grid rectangle B_N by B changes only
O(1/N)-wide boundary strips, which have the same strict exponential
gap. This is the finite-window counterpart of suppressing all
nonzero Poisson modes; no infinite-lattice replacement was made.

Finally deform that integral to

    x_*(chi)+(B-x_0).

This translation remains inside the same holomorphic tube. Its
endpoint connectors have the boundary gap. On the translated box,
Re(f(x_*+u,chi)-phi(chi))<=-c|u|^2 uniformly for real u, since
A(chi) remains close to a positive definite real matrix. Taylor
expansion and Gaussian integration give the stated determinant.
The nominal N^-1/2 corrections are odd in u and integrate to zero
on the symmetric Gaussian domain; truncation errors are exponentially
small. The remaining relative error is O(N^-1), including the
uniform b_N-b error. This proves (9) for the exact finite packet,
not merely for real parameter values or a selected subsequence.

## 4. The Conway packet and its color Hessian

Apply (9) with a=3-H and d=2H-3. There is a fixed complex chi
polydisk on which

    Z_N^win(chi)=N^(3/2) a_E(chi) exp[Nphi_E(chi)]
                                         [1+O(N^-1)],          (11)
    a_E(chi)=(2pi)^((2H-3)/2)
            b(x_*(chi),chi)/sqrt(det A(chi)).                  (12)

The amplitude is nonzero and a_E(0)>0. This is the raw source
normalization in the stated free integer coordinates. Any separately
recorded enhancement or framing phase must still multiply it;
(11) does not remove such a factor from an invariant.

All statements hold on the whole sequence of sufficiently large N,
including both parities. The upper leaf cutoff floor((N-1)/2) lies
outside the fixed strict window. Half-grid endpoint choices affect
only exponentially small boundary terms, and (2) has no parity-
dependent lattice density. The canonical factorial normalization
has fixed the actual square roots and the offset factors in (6).

The phase and amplitude are separately even in each chi_l. Indeed
f and the summand have this symmetry, and uniqueness of the local
critical branch gives the same symmetry for x_*. At completeness,

    phi_E(0)=max V_E/pi,
    partial_(chi_l) phi_E(0)=0,
    partial_(chi_l)partial_(chi_m) phi_E(0)
       =-2pi cot(pi x_(l,*)) delta_lm.             (13)

To verify the last formula, f_(x chi_l)(x,0)=0 IDENTICALLY in x,
because each leaf factor is even in its own parameter. Hence the
usual critical-point Schur-complement correction vanishes here.
The direct second derivative of (8) is -2pi cot(pi x_l).
Every x_(l,*) is in (0,1/2), so this Hessian is strictly negative.
Uniformity on a complex disk also supplies every fixed color
parameter derivative by Cauchy estimates on a smaller disk.

## 5. Comparison with the positive core, and the remaining interfaces

For physical real deficits in a sufficiently small fixed window,
the positive core outside B is exponentially smaller than the
complete source at chi=0. Indeed each exact deformed core coefficient
is at most its complete counterpart, the product coefficients are
positive, and the complete action has a strict compact support gap
outside B. The polynomial number of states and the uniform global
factorial estimates preserve that gap. Therefore

    |Z_N^core(h)-Z_N^win(h/N)|
                      <=poly(N) exp[N(phi_E(0)-gamma)]          (14)

with gamma>0. Shrink the real color window so phi_E(h/N) stays
above phi_E(0)-gamma/2. Equations (11),(14) then give exponential
relative accuracy for the WHOLE positive core.

A separate uniform estimate for the signed alias sectors can be
combined with (14); the present proof does not assume such sectors
are absent. Nor does the complex window argument identify chi with
a geometric meridian or establish the Dehn-filling contour. It
supplies the exact even analytic core packet, its nonzero marked
amplitude, its all-parity normalization and its uniform complex
saddle expansion, which those later steps require.

## 6. An explicit three-leaf calibration, including the integer shift

For the retained seed C(h^3), use the three original leaf indices
i,j,k as free coordinates. The surviving gate output is EXACTLY
t=D-k. Thus its limiting output is z=1-x_3, but its interpolated
factorials have the additional shift -1 in t. The limiting phase is

    F(x_1,x_2,x_3)=sum_l g(x_l)+m(x_1,x_2,1-x_3).

Its unique maximum occurs at all three x_l=a=atan(2)/pi. Directly,

    sin(pi a)=2/sqrt(5), sin(2pi a)=4/5,
    sin(pi(3a-1))=2/(5sqrt(5)),
    g'(a)=m_z(a,a,1-a)=-log4,
    m_x(a,a,1-a)=m_y(a,a,1-a)=log4.

These give stationarity in the actual three free coordinates. The
negative Hessian and its positive determinant square root are

    A=(25pi/4)(I_3+1 1^T),
    sqrt(det A)=125pi^(3/2)/4.                              (15)

Each unshifted leaf amplitude in (5) is sqrt(10)/8; the unshifted
gate amplitude is 5sqrt(10)/16. The actual output t=N(1-x_3)-1
adds the factor exp(-m_z)=4. Equivalently its seven factorial
shifts are 0,-1,0,0,-1,-1,+1 in the displayed numerator/denominator
order of the exact Newton coefficient

    mu_(N;i,j,t)=s_(i+j)s_t
                    /[s_i s_j s_(t-i)s_(t-j)s_(i+j-t)].

Thus

    b(a,a,a,0)=(sqrt(10)/8)^3 (5sqrt(10)/16) 4=125/512,
    a_(h^3)(0)=(2pi)^(3/2)b/sqrt(det A)=sqrt(2)/64.          (16)

Omitting D=N-1's shift would give a leading amplitude four times
too small. This makes the shift convention in (2),(5) testable.
The phase is F_0=3g(a)+m(a,a,1-a)=2v_8/pi, using the already
proved [whole three-leaf seed evaluation](actual_positive_conway_variational_limit.md).
Hence the theorem above and the positive-core comparison give

    Z_(h^3,N)=(sqrt(2)/64)N^(3/2)exp(2Nv_8/pi)(1+O(N^-1)). (17)

The audit derives the gradient, Hessian, determinant and amplitude
from the individual signed factorial arguments using exact rational
and radical arithmetic. It also evaluates the original positive sum

    sum_(0<=i,j,k<=M; i+j+k>=D)
        a_(N,i)a_(N,j)a_(N,k) mu_(N;i,j,D-k).

For N=5,8,20,40,80 its ratios to the leading term of (17) are
1.44279, 1.26530, 1.10276, 1.05067 and 1.02515. Additional levels
21,41,81 check the odd sequence. These finite values are diagnostics
of the independently proved normalization, not an extrapolation
argument for (17) or the complex-window theorem.

Audit: [exact calibration and finite positive sums](../experiments/audit_actual_conway_complex_window_laplace.py)
and [results](../experiments/actual_conway_complex_window_laplace_results.json).

The complex-window argument retains the primitive lattice count, integer offsets and finite contour errors. It requires the separate source-algebra and alias results.

The [whole-source assembly](actual_conway_long_filling_source_limit.md) combines this packet with separately proved alias and marked geometric results.