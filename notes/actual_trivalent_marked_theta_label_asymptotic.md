# Whole-label asymptotic of the original signed marked theta source

29 October 2026. The exact coherent magnetic contraction in the
[all-channel marked theorem](actual_trivalent_all_channel_marked_contraction.md)
gives a sharp positive partition before any estimate. This note proves
its entire-label gap and the nonzero Gaussian asymptotic after ANY
fixed signed twists on its three original pair edges. Both parities,
the odd simple endpoint weight, paired-circle first normals and the
sole physical marked normal are retained. No complement geometry or
arbitrary graph sewing theorem is inferred.

## 1. Actual raw source and the theorem

Set N>=2, d=N-1, q=exp(pi i/N), Q=q^2, kappa=q^(d^2/2),
m=d/2, M=floor(m), and s_u=product_(r=1)^u 2sin(pi r/N).
For physical folded labels 0<=j_i<=M put J=sum j_i, delta=J-d,
and r_i=J-2j_i. Let k_j=2 except at the odd simple node j=m,
where k_j=1. The EXACT marked raw channel contribution is

    Z_N(j)=N^2 product_i k_(j_i)
                   *[product_i s_(r_i)/s_delta] R_N(j)^2, J>=d,
    Z_N(j)=0,                                                   J<d. (1)

Here R_N is the proved finite factorial partition. Formula (1)
has already summed EVERY magnetic index with the genuine ordinary
white dual and original unrestricted physical marked row. It is not
the black tensor's Euclidean norm. There is no outside component
normalization in this raw source.

Insert the original R^(e_i)L_N on edge i, for arbitrary FIXED signed
integers e_1,e_2,e_3. The raw whole source is exactly

    Theta_N(e)=sum_j Z_N(j) product_i omega_(j_i)^(e_i),
    omega_j=kappa(-1)^j q^[j(j+1)].                    (2)

This includes the full original Cartan scalar. A separately recorded
external line factor chi_N remains outside Theta_N.

Put j0=v8/pi=8 Lambda(pi/4)/pi and define the literal unit phase

    Omega_N=kappa exp(i pi d/2) q^[m(m+1)] (-1)^d,
    q^r means exp(i pi r/N), including fractional r.

Then

    Theta_N(e)=N^(3/2) exp(2N j0) Omega_N^(e_1+e_2+e_3)
       /[16 product_i sqrt(2-i e_i)] *[1+O_e(1/N)].    (3)

EACH square root has positive real part. Equivalently choose the
determinant square root by continuation from e=0. The principal
square root of the product can have the WRONG SIGN for large
same-sign twists, for example e=(5,7,9). The leading constant in
(3) is nonzero. Thus for both parities and composite levels

    lim_(N->infinity) (2pi/N)log|Theta_N(e)|=4v8.      (4)

This is an actual source limit. It is not a claim that its complement
has volume 4v8 absent a separate literal topological certificate.

## 2. A whole-label strictly concave action

Let L(x)=integral_0^x log(2sin pi u)du and set

    sigma_i=(m-j_i)/N,
    x_i=1/4+sigma_i-(sum sigma)/2, i=1,2,3,
    x_4=1/4+(sum sigma)/2.

The physical supported set has sigma_i>=0, sum sigma_i<=m/N;
all four x_i lie in (0,1/2) and sum x_i=1. On the compact limiting
support the endpoints are included by continuity.

The established scalar partition has rate
Phi=-(2)sum_(i=1)^4 L(x_i). Its extra weight in (1) has rate
sum_(i<=3)L(2x_i)-L(1-2x_4)=sum_(i<=4)L(2x_i).
Consequently the complete channel contribution has action

    E(sigma)=sum_(i=1)^4[L(2x_i)-4L(x_i)]
            =sum_(i=1)^4 h(x_i),
    h(x)=-2[L(x)+L(1/2-x)].                          (5)

The last equality follows from the elementary duplication and
reflection identities for L. DIRECTLY

    h(1/2-x)=h(x),
    h''(x)=-4pi/sin(2pi x)<0, 0<x<1/2.             (6)

Hence h is strictly concave, with unique maximum at x=1/4.
Equation (5) has its UNIQUE maximum at sigma=0, with

    E(0)=2j0, Hess_sigma E(0)=-4pi I_3.             (7)

The four tetrahedral sign rows mapping sigma/2 to x-1/4 have
orthonormal columns. Flipping ANY one sigma_i takes that row set
to the negatives of a permutation of itself. Together with (6)
this proves E is SEPARATELY EVEN in every sigma_i, not merely
stationary at zero. In particular

    E(sigma)=2j0-2pi sum sigma_i^2+O(||sigma||^4).     (8)

The uniform all-index O(log N) sine-factorial estimate, including
zero indices, and the at-most-N inner R sum give

    log[Z_N(j)/product_i k_(j_i)]=N E(sigma)+O(log N) (9)

uniformly on the ENTIRE supported physical set. The actual half-step
in m only changes this global estimate by O(log N). All forbidden
labels contribute zero exactly. By compactness and strictness of
(7), for every fixed rho>0 there is gamma_rho>0 such that

    sum_(max sigma_i>=rho) Z_N(j)
                  <=poly(N)exp[N(2j0-gamma_rho)].    (10)

Thus a complete physical-label complement is exponentially small.
Since every physical twist in (2) has modulus one, the SAME bound
controls the signed source complement before any cancellation.

## 3. Uniform local prefactor, including the three half-steps

The exact complex scalar partition theorem gives, uniformly on a
fixed small sigma polydisk,

    Rwin_N=N^(-3/2)exp(NPhi)
                  /[4sqrt(product_i cos(pi sigma_i))]*(1+O(1/N)).

Its actual physical omitted terms have a strict gap. The remaining
sine factors in (1) have indices

    r_i=2N x_i-1/2,
    delta=N(1-2x_4)-1/2.

The canonical half-shifted factorial formula
S_hat_N(Na-1/2)=sqrt(N)exp[NL(a)](1+O(1/N))
therefore gives

    product_i s_(r_i)/s_delta
       =N exp{N sum_(i=1)^4 L(2x_i)}*(1+O(1/N)).

The N^2 in (1), this N, and Rwin_N^2's N^-3 cancel EXACTLY.
Thus locally on the physical lattice

    Z_N(j)=product_i k_(j_i)
       *exp[N E(sigma)]/[16 product_i cos(pi sigma_i)]
                                                   *(1+O(1/N)). (11)

The error is uniform on a fixed corridor. On a smaller corridor,
real coercivity E<=2j0-c||sigma||^2 holds. The known exact complex
factorial window also gives bounded fixed derivatives, but no
off-grid identification with auxiliary meridians is needed here.

## 4. Exact signed twist chirp and parity unfolding

At EVERY physical folded label,

    omega_j=Omega_N exp(i pi N sigma^2).             (12)

Indeed j=m-Nsigma and 2m+1=N. Writing (-1)^j=exp(pi i j), the
q exponent difference between the two sides of (12) is
-2N(d-j), an integer multiple of 2N. This proves (12) with its
literal fractional root, not an arbitrary choice of sqrt(kappa).

If N is odd, Nsigma is an integer >=0 and the zero point has weight
one while every positive point has weight two. If N is even,
Nsigma lies in Z+1/2, is positive, and every point has weight two.
Thus the k_j weights unfold any EVEN leading integrand EXACTLY to
the full integer respectively half-integer lattice. Their product
unfolds all three directions. The supported simplex boundary is a
fixed distance from zero, so extending the local Gaussian lattice
to infinity has an exponential error.

Insert (8),(11),(12) into (2). Quartic action errors contribute
relative O(1/N) after absolute Gaussian integration, because
N||sigma||^4 has Gaussian mean O(1/N). The even amplitude's error
is O(||sigma||^2), with the same O(1/N) expectation. Uniform
factorial errors in (11) are O(1/N) already. The fixed signed chirp
has modulus one on the real grid, so these absolute error estimates
remain valid. Equation (10) controls the rest of the original sum.

For A_i=2-i e_i, Re A_i=2. The one-dimensional exact Gaussian
Poisson identity gives, with epsilon=0 or 1/2,

    sum_(h in Z+epsilon) exp[-pi A_i h^2/N]
      =sqrt(N)/sqrt(A_i)
        *sum_(ell in Z)exp[-pi N ell^2/A_i]exp(2pi i ell epsilon).

Its nonzero Fourier modes are exponentially small because
Re(1/A_i)=2/(4+e_i^2)>0. Multiply the three identities and the
factor 1/16 from (11). This proves (3), including its nonzero
phase, N^(3/2), both parity cosets and every fixed signed triple.
No uniform assertion for twists growing with N is made.

## 5. Source and geometry scope

The magnetic growth of an individual black vertex has been contracted
COHERENTLY with the actual white/marked source before (1). This
positive partition is specific to that two-vertex wiring. Formula
(3) does not make arbitrary white vertices adjoints, does not bound
an arbitrary branched graph in a tensor-product norm, and does not
identify a spectral channel parameter with a peripheral color.
Any hyperbolic-volume conclusion still needs the complement's
separate literal geometric certificate and original external line.

That separate certificate is now given in
[the actual theta-link and angle geometry](actual_marked_theta_link_and_angle_geometry.md):
the literal source is the three-box augmented pretzel matching, its
complete complement has four regular ideal octahedra for every fixed
signed e, and the original reduced one-cut external line has modulus
one. Together with (3), it identifies (4) with the ACTUAL complement
volume for that complete link family. It does not prove a filled-knot
statement or general open-graph source factorization.

Audit: [exact phases/folding and all-parity whole-label sums](../experiments/audit_actual_trivalent_marked_theta_label_asymptotic.py).

Root's independent analytical review passed the whole-label action,
strict gap, actual half-step prefactor, separate evenness, both parity
folds, literal Omega_N and each Gaussian square-root branch, including
the relative O_e(1/N) error. A fresh primary audit passed 4,159 exact
rational root-phase checks, 127 exact parity-fold families, symbolic
action identities and six complete-label families with 24 coherent
signed profiles. The separately proved full-normal marked source
identity is the input; numerical profiles supplement this proof.
