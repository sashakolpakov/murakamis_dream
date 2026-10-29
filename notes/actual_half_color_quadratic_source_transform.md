# A finite half-color quadratic transform for the original source

29 October 2026. This proves the exact simple-channel coefficient
of the ORIGINAL figure-eight four-plat in the complete Casimir frame.
The finite proof uses one terminating q-Chu identity, proved below by
finite binomial expansion. It retains all root phases, common Cartan
factors and the actual original cup/cap opening.

The resulting coefficient is a positive sine-binomial square sum
times its known phase. It tests the pointed energy of the complete
channel Gram, not the value of the invariant after its final cap.

## 1. A reusable odd-root quadratic transform

Let `N=2m+1>=3`, let Q have exact order N, put
`F_r=(Q;Q)_r` and `a=Q^(-m)=Q^(m+1)`. All factorials below
have index at most 2m and are nonzero. Define

    S_m=sum_(k=0)^m Q^[-k(m-k)] [m choose k]_Q^2.

Then EXACTLY

    sum_(t=0)^m Q^t (a;Q)_t^3/F_t^2
       =(-1)^m Q^[-m(3m+1)/2] S_m.                 (1)

This is a finite 3-parameter-to-2-parameter quadratic source
transform. It is valid at composite odd levels as well as prime
ones, with no square-root choice or root-zero denominator.

Proof. Expand the THIRD Pochhammer by the finite binomial theorem,
put `t=k+j`, `n=m-k`, and retain the other two factors. The left
side becomes

    sum_(k=0)^m (-a)^k Q^[k(k-1)/2+k](a;Q)_k^2/F_k^2
       *sum_(j=0)^n Q^j (aQ^k;Q)_j^2
                                      /[F_j(Q^(k+1);Q)_j].

Apply terminating q-Chu to the inner sum with terminating length n,
`b=Q^-n=aQ^k`, `c=Q^(k+1)`. It is

    Q^(-n^2)(Q^(m+1);Q)_n/(Q^(k+1);Q)_n
       =Q^(-n^2)(a;Q)_n F_k/F_m.                   (2)

Here the ODD ROOT relation `Q^(m+1)=a` is essential. Substitute

    (a;Q)_r=(-1)^r Q^[-mr+r(r-1)/2]F_m/F_(m-r).

Each k-th term is now
`(-1)^m Q^[-m(3m+1)/2-k(m-k)] [m choose k]_Q^2`.
This proves (1), including every sign and exponent.

## 2. Elementary finite q-Chu and Durfee identities

The finite identity used in (2), whenever its denominators are units,
is

    sum_(j=0)^n (Q^-n;Q)_j(b;Q)_j Q^j
                                  /[F_j(c;Q)_j]
       =b^n(c/b;Q)_n/(c;Q)_n.                     (3)

No published summation proof is a premise. Here is a direct finite
proof. First the binomial theorem gives

    sum_(s=0)^n (Q^-n;Q)_s Q^s/F_s
                               *(cQ^s;Q)_(n-s)
       =(-c)^n Q^[n(n-1)/2].                      (4)

To check (4), expand the last Pochhammer. Its c^r coefficient
contains `(Q^(1-(n-r));Q)_(n-r)`, zero unless r=n. Only that
last coefficient survives, giving the right side.

Multiply (3) by `(c;Q)_n`, expand `(b;Q)_j`, and extract b^r.
Set `j=r+s` and apply (4) with length n-r and parameter cQ^r.
The result is

    (-c)^(n-r) Q^[(n-r)(n-r-1)/2][n choose r]_Q,

the b^r coefficient of `b^n(c/b;Q)_n`. Thus (3) is a rational
identity before specialization and holds at the stated roots.

Its useful finite Durfee consequence is

    sum_(r=0)^t Q^(r^2)/(F_r^2 F_(t-r))=1/F_t^2.   (5)

Indeed take n=t, b=Q^-t, c=0 in (3), multiply by Q^(t^2),
and reverse its summation index. This proves (5) by the same
finite algebra, without an infinite-product interpretation.

## 3. The actual complete-channel coefficient

Now use the principal `q=exp(pi*i/N)`, `Q=q^2`, `d=2m`,
`x=q^d=Q^m`, `nu_m=(-1)^m q^[m(m+1)]`. Let R_1,R_2 be the
two ORIGINAL generators on the complete source multiplicity module,
including their common Cartan kappa. The TRUE four-plat action order
is `[2,-1,2,2]`, hence

    W=R_2^2 R_1^(-1) R_2.

Let V be the complete physical Casimir/Hermite frame, J the actual
anti-Pascal recoupling, and p the original cup. Define the COMPLETE
right-channel output

    z=V^(-1)J Wp.

At odd N the node c=-2 is simple, with normalized eigenvector
`f_0=1`, crossing value nu_m and bilinear norm `sigma=x^d nu_m`.
Its exact coefficient is

    z_simple=N Q^[m(m+1)] F_m S_m.                  (6)

At the principal root `S_m=sum_(r=0)^m |[m choose r]_Q|^2>0`.
Thus (6) is not an expanded path or a guessed saddle surviving
selection; it is the ENTIRE actual channel after all its sums.

## 4. Source reduction to the quadratic transform

The actual J is symmetric: its anti-Pascal formula and
`F_jF_(d-j)=N(-1)^jQ^[j(j+1)/2]` give `J_(i,j)=J_(j,i)`.
Put `y=Jf`, `h=R_2p`, `v=R_1^(-1)h`.
The lower bidiagonal equation for y, with endpoint `y_d=f_0=1`,
gives exactly

    y_i=0 for i<m,
    y_(m+r)=Q^[-r(m-r)][m choose r]_Q^2.             (7)

The successive ratio is the square of
`|1-Q^(m-r)|/|1-Q^(r+1)|`; its complex factorial form in (7)
keeps the phase identity at arbitrary primitive Q.

The FIRST original R_2 on the cup highest lift has a forced final
third-head color zero. In the literal positive crossing the transfer
must equal that second input color. Its coefficient simplifies to
`kappa F_(d-i)`, using `x^2=Q^-1`. Therefore

    h_i=kappa p_i F_(d-i), p_i=Nx^(i-d).            (8)

The literal original inverse crossing then gives

    v_i=x^(i-d)(-1)^i Q^[i(i+1)/2-d] F_(d-i)/F_i
                         *sum_(b=i)^d Q^b F_b^3/F_(b-i).     (9)

For example (9) follows directly by the finite inverse-R transfer
sum and the SAME reflection identity; the common kappa in (8)
cancels the prescribed inverse kappa. No external normalization
has been changed.

Multiply (9) by (7), put `i=m+r`, and interchange `b=m+t` and r.
Using (5) gives

    y^T v=C sum_(t=0)^m Q^(m+t) F_(m+t)^3/F_t^2,
    C=(-1)^m x^(-m) Q^[m(m+1)/2+1].                 (10)

This intermediate reduction is a finite identity with the original
source; in particular no extension beyond the true finite ranges
has been made. Since `F_(m+t)=F_m(a;Q)_t`, (1) evaluates (10):

    y^T v=Q^[-2m^2+m+1]F_m^3 S_m
           =F_m^3S_m=N nu_m F_m S_m.               (11)

The remaining exponent is `(1-m)(2m+1)`, a full root period.
The last equality is the full reflection identity `F_m^2=N nu_m`.

Finally the simple inverse channel row is `f^T/sigma`. Moving the
two terminal R_2 factors through J and selecting that simple channel
gives

    z_simple=(kappa^2 nu_m^2/sigma)y^T v
             =nu_m y^T v.

Here `kappa^2=x^d` for the actual odd-level full Cartan. Substituting
(11) proves (6), with all source and common-line phases retained.

## 5. Scope for the proposed positive energy

For the balanced complete-channel Gram
`G=(V^(-1)J)^*(V^(-1)J)/N`, the original pointed energy is
`E_N=N^(-1)||z||_2^2`. Equation (6) implies EXACTLY

    E_N>=N^2 S_m^2,                                 (12)

because `|F_m|^2=N`. The asymptotic consequence is developed in
the companion energy audit; it concerns THIS particular positive
Gram. It does not contradict its exact Cauchy inequality, and it
does not rule out a different source-preserving coherent terminal
Gram that contracts more of the actual tensor before squaring.

[Audit](../experiments/audit_actual_half_color_quadratic_source_transform.py):
the finite q-Chu/quadratic transform and the literal full original
four-plat simple-channel coefficient, at odd composite and prime
levels, with all common Cartan and source constants.
