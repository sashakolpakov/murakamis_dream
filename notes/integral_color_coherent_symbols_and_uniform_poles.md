# Actual integral-color coherent symbols, uniformly including the poles

Research proof, 27 October 2026. The actual integral N-color family
admits a globally regular polynomial source frame. Its generator
symbols have exact finite formulas and uniform expansions on the
entire real compact source, including both poles. Moving q and
the integral color together gives the expected exponential clock.
An explicit flag shear compares its principal moment matrix with
the varying-meridian Grothendieck chart.

Every change of frame below is an exact diagonal quantum-factorial
change of the actual representation and source. Its large size
cannot be discarded when comparing selected periods. Uniform
asymptotics of the individual generators do not prove uniform
asymptotics of the full R word.

The exact symmetric whole-q-difference model is developed in
[the global integral-color source note](integral_color_global_q_difference_source.md).
The quantitative frame norm, its dilogarithmic generating
function, and the root flag-current bookkeeping are given in
[the quantum-factorial source comparison](quantum_factorial_frames_and_cyclotomic_source.md).

## 1. The actual integral family and its polynomial frame

Fix N>=2, put n=N-1, and use

    c=2pi*i, s=c lambda, 0<=lambda<=1,
    q=exp(s/(2N)), Q=q^2, rho=q-q^(-1),
    M=-q^N, m=q^N=exp(s/2).

Write `[j]_q=(q^j-q^(-j))/rho`, with its Laurent-polynomial
continuation when rho=0. In the ordinary-falling polynomial
frame the actual integral module has

    F e_j=(n-j)e_(j+1),
    E e_j=[j]_q[N-j]_q/(N-j)e_(j-1),
    K e_j=q^(n-2j)e_j.                         (1)

The absent boundary edges are zero. Put Ecal=rho E and Fcal=rho F.
These are the operators compared below. They satisfy exactly

    K Ecal K^(-1)=Q Ecal, K Fcal K^(-1)=Q^(-1) Fcal,
    Fcal Ecal+qK+q^(-1)K^(-1)=(q^N+q^(-N))I.    (2)

For example the diagonal entry of Fcal Ecal is
`rho^2[j]_q[N-j]_q`; expanding the two q-numbers proves (2).

Use the same actual compact coherent kernel as before:

    sigma_C(v,z)=sum_(i,j=0)^n v^i C_ij binom(n,j)z^j
                                                   /(1+vz)^n.

Its globally regular source coordinates are

    T=vz/(1+vz), a=z/(1+vz), b=v/(1+vz),
    ab=T(1-T), a=T/v, b=v(1-T),
    Omega_0=dv wedge da.

On the compact real source `z=bar(v)`, both |a| and |b| are at
most one half, and 0<=T<=1. The pole-chart change is
`V=1/v, a'=v-v^2a`.

## 2. Exact finite-N symbols have no polar singularities

Let

    R_x(T)=1+(x-1)T,
    W_N(T)=q^N+q^(-N)-q^(-N)R_Q(T)^N
                              -q^N R_(Q^-1)(T)^N.

Then the exact actual symbols are

    sigma_K=q^n R_(Q^-1)(T)^n,
    sigma_(K^-1)=q^(-n)R_Q(T)^n,
    sigma_A=R_Q(T)^n, A e_j=Q^j e_j,
    sigma_Fcal=n rho b,
    sigma_Ecal=a H_N(T),
    H_N(T)=W_N(T)/[N rho T(1-T)].               (3)

The apparent divisions in the last formula are removable.
Indeed W_N is a polynomial which vanishes exactly at T=0 and
T=1, so it is divisible by T(1-T). It is also divisible by
rho^2 as a Laurent polynomial in q, making rho=0 removable.
Its two endpoint values agree:

    H_N(0)=H_N(1)=q^n-q^(-n).                  (4)

Thus (3) is a globally regular source function, including its
two pole fibers, not just a formula on the open torus.

Here is the short coefficient proof. In the Ecal kernel use

    binom(n,j)/(N-j)=binom(N,j)/N,
    rho^2[j]_q[N-j]_q
       =q^N+q^(-N)-q^(2j-N)-q^(N-2j).

Extend the sum to j=0,N, where its summand is zero. The binomial
theorem gives W_N divided by `N rho v(1-T)`; since `T/v=a`,
this is exactly (3). The Fcal formula follows from
`sum_j(n-j)binom(n,j)x^j=n(1+x)^(n-1)`.

## 3. Uniform asymptotics hold on the entire compact source

Define the whole principal functions

    A_inf=exp(sT), k=m exp(-sT),
    f=s b,
    W(T)=m+m^(-1)-k-k^(-1)
        =4sinh(sT/2)sinh(s(1-T)/2),
    H(T)=W(T)/[sT(1-T)], e=a H(T).              (5)

Every apparent division in (5) is removable, including s=0.
For each fixed nonnegative integer l there is a finite constant
C_l, independent of N and lambda in [0,1], such that in smooth
coordinate norms on the whole real compact source

    ||sigma_A-A_inf||_(C^l)
      +||sigma_K-k||_(C^l)
      +||sigma_(K^-1)-k^(-1)||_(C^l)
      +||sigma_Ecal-e||_(C^l)
      +||sigma_Fcal-f||_(C^l) <= C_l/N.         (6)

The following proof includes the endpoint estimates. For fixed
S and l, the binomial exponent has the elementary bound

    ||R_(exp(s/N))(T)^N-exp(sT)||_(C^l[0,1])
                                      <=C_(S,l)|s|^2/N    (7)

for |s|<=S. For large N expand the logarithm of
`1+(exp(s/N)-1)T`; its difference from sT/N and its fixed
T derivatives are uniformly bounded. Alternatively differentiate
the binomial power explicitly. The two first s coefficients
are identical, giving the |s|^2 factor. The finitely many smaller
N have the same bound by compactness after dividing out s^2.

Apply (7) to W_N-W with two extra T derivatives. This difference
vanishes at both endpoints. For any such function g,

    g(T)/[T(1-T)]
      =-T integral_0^1 y g''(Ty)dy
       -(1-T)integral_0^1 y g''(1-(1-T)y)dy.    (8)

Differentiation of (8) bounds its C^l norm by a fixed multiple
of the C^(l+2) norm of g, with no endpoint loss. Moreover
`N rho/s=sin(pi lambda/N)/(pi lambda/N)` is bounded below by
2/pi on this family. Equations (7)--(8) therefore give

    ||H_N-H||_(C^l[0,1])<=C_l |s|/N.

The corresponding Fcal bound follows from
`n rho=s+O(|s|/N)`. The K and clock estimates use (7) and the
one missing power n=N-1. Multiplication by the globally smooth
functions a,b proves (6) in both compact pole charts. This also
proves uniformity at lambda=0; it does not divide a nonzero
estimate by a vanishing rho without its |s| factor.

The exact star product is still required for finite matrices.
Ordinary products of symbols equal the classical products only
in this controlled principal limit. In particular (2) gives the
principal Casimir identity `ef+k+k^(-1)=m+m^(-1)`.

## 4. The moving-q clock and the actual principal moment matrix

The actual simultaneous path has `M=-q^N=-m`, so the principal
Gauss parameter is x=-M=m. Its clock is precisely

    A_inf=exp(sT), k=x/A_inf.                  (9)

Thus moving q really changes its frequency from c to c lambda.
Changing only M at fixed q_N would not do that.
Where its factors are nonzero, the old balanced momentum is

    p_bal=(1-A_inf)/f
         =(1-exp(sT))/[s v(1-T)].             (10)

The full moment matrix is globally regular even where this
particular momentum chart fails:

    mu=[k,e;k f,m+m^(-1)-k], det mu=1.         (11)

Its eigenvalues are m and m^(-1). The actual knot-meridian sign
in the old convention is `-mu`, since M=-m. At lambda=1 its
projective sign gives the complete physical meridian. All M and
SL2 sign markings are retained; choosing one of the two eigenflags
is additional augmented data.

For the m-eigenflag use the slope v_geo in `[1:v_geo]`. Directly,

    v_geo=(m-k)/e=k f/(k-m^(-1))
          =r_s(T)v,
    r_s(T)=s(1-T)/(1-exp[-s(1-T)]).           (12)

Consequently (11) is exactly the whole Grothendieck matrix from
[the exponential detour](compact_exponential_cech_current_detour.md)
evaluated at `(T,v_geo)`. The source shear

    (v,a)->(r_s(T)v,a/r_s(T))

preserves T and Omega_0 exactly, because
`Omega_0=-dT wedge dlog v`. For lambda<1 it is regular on the
whole real compact sphere. In this ordinary-falling frame it
becomes singular at lambda=1,T=0. This particular singularity
is frame dependent, as the next section proves.

The other eigenflag, corresponding to the original inverse-cut
marking `M^(-1)=-m^(-1)` on `-mu`, has slope

    v_inv=s v(1-T)/(1-exp(sT)).                (13)

Equations (12)--(13) must not be silently interchanged.

## 5. An exact quantum-factorial change removes the first flag artifact

The symmetric q-falling frame has

    E_q e_j=[j]_q e_(j-1), F_q e_j=[n-j]_q e_(j+1).

Its change from (1) is diagonal. If `e'_j=g_j e_j`, then

    g_0=1, g_(j+1)/g_j=(n-j)/[n-j]_q.

All these factors are nonzero on 0<=lambda<=1. The exact finite
symbols in this frame are

    sigma_(rho E_q)=[R_q(T)^n-R_(q^-1)(T)^n]/v,
    sigma_(rho F_q)=v[q^nR_(q^-1)(T)^n-q^(-n)R_q(T)^n].    (14)

Their endpoint divisions are removable, and the same elementary
binomial argument proves uniform C^l convergence on the entire
compact sphere to

    e_sym=2sinh(sT/2)/v,
    f_sym=2v sinh(s(1-T)/2), k=m exp(-sT).       (15)

The m-eigenflag now has the regular slope

    v_+=exp(s(1-T)/2)v,                        (16)

through lambda=1, including both poles. The inverse eigenflag is

    v_-=-exp(-sT/2)
            sinh(s(1-T)/2)/sinh(sT/2) v.       (17)

For lambda<1 it reverses the two pole flags, whereas at lambda=1
the ratio of the two sines is one and (17) equals (16). The
two corner limits `(lambda,T)=(1,0),(1,1)` therefore retain the
inverse-flag collision/bubble data. Regularity of (16) does not
justify deleting that augmentation information.

The exact principal comparison is

    b_s(T)=2sinh(s(1-T)/2)/[s(1-T)],
    e=b_s e_sym, f=f_sym/b_s.                 (18)

Equivalently use the symplectic source shear
`v_sym=v/b_s(T), a_sym=b_s(T)a`. At lambda=1,T=0, b_s vanishes;
the ordinary-frame pole in (12) is thus a basis artifact.
These are exact matrix and principal-coordinate comparisons,
not a boundedness assertion about the changing frame.

## 6. The original balanced word and pointed source are retained exactly

There is also an explicit exact adapter to the existing balanced
integral module. In that frame

    F_bal v_j=(1-Q^(j+1))v_(j+1),
    Ecal_bal v_j=(M Q^(-j)-M^(-1))v_(j-1).

At M=-q^N define

    d_j=(Q;Q)_j/[rho^j(n)_j]
       =(-1)^j q^(j(j+1)/2)[j]_q!/(n)_j,
    D=diag(d_j), d_0=1.                       (19)

Here `(n)_j=n(n-1)...(n-j+1)`. The second expression makes
lambda=0 removable, with value `(-1)^j j!/(n)_j`. Every d_j
is nonzero on the full real path, including lambda=1. Directly,

    D^(-1)F_bal D=rho F,
    D^(-1)Ecal_bal D=rho E,
    D^(-1)K D=K.                              (20)

For the second identity use
`M Q^(-j)-M^(-1)=-rho q^(-j)[N-j]_q`. Thus (20) is an exact
quantum-factorial frame of the actual integral representation,
not a newly ordered classical polynomial.

Conjugating every strand by D conjugates every actual factorial
R matrix by `D tensor D`. The Cartan factor, pivot, transfer
weights and head projectors are kept; the diagonal factors
commute with the latter three. Internal D factors telescope
through an arbitrary word. Its cut matrix transforms as

    C_poly=D^(-1)C_bal D.

The literal rank-one source transforms at the same time:

    psi_poly=D^(-1)psi_bal, phi_poly=phi_bal D.              (21)

All pointed pairings are therefore exactly unchanged. For every
weighted knot word the cut matrix is diagonal by integer-weight
conservation, so its actual normalized source is also its same
normalized trace before and after (20). The weighted Green
current identities are preserved coefficientwise.

The genuine integral Hopf pivot K and the original auxiliary
root-compatible pivot `K^(1-N)` must still be distinguished.
Their exact closed-strand adapter is `K^(-N)`. It commutes with
every displayed diagonal change of frame and remains an actual
position-dependent insertion off the root:

    K^(-N)e_j=q^(-Nn)q^(2Nj)e_j.

At q_N it becomes the retained scalar `(-1)^n`; along the
moving-q path it cannot be replaced by that value. The external
modified-dimension and framing factors likewise stay their
original ones. The basis identity does not equate two generic
quantum invariants whose pivots or external source factors
were chosen differently.

Equation (20) does not license replacing (21) by an unrelated
vacuum or discarding the size of D in asymptotics. Likewise the
symmetric q-falling adapter and its source must be retained.
Their quantum-factorial norms can carry exponential size. The
individual uniform generator bounds (6) and (15) prove neither
a uniform full-word star expansion nor the selected geometric
period. They give the exact source frames and global classical
moment maps to which such a theorem would have to apply.

## 7. Exact audit and endpoint checks

[audit_integral_color_coherent_symbols.py](../experiments/audit_integral_color_coherent_symbols.py)
and its
[results](../experiments/integral_color_coherent_symbols_results.json)
verify all finite symbols, removed endpoint values, Casimir
normalization, and both diagonal frame adapters at levels 2
through 6 over the rational function field in q. They also
check the two principal augmented flags and ordinary/symmetric
shear identities.

A separate 70-digit grid check uses N=8,16,32,64,128, includes
lambda=0,1, both exact T endpoints, nearby T=10^(-8), and the
color-scale endpoint positions T=1/N,1-1/N. It agrees with the
proved uniform rate. These numerical checks audit conventions
and cancellation; the uniform whole-sphere assertion is the
argument (7)--(8), not an extrapolation from that grid.
