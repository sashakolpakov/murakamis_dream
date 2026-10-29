# An actual noncentral trivalent source packet with two Steinberg legs

29 October 2026. The odd central quartic transform extends to EVERY
retained node on one leg of the ORIGINAL black trivalent source, with
the other two legs central. It gives an exact common-phase positive
factorial sum, a fixed complex color packet, and a strict physical
complement gap. This is one actual magnetic coefficient, not a
replacement for the full three-channel vertex or its white/marked rows.

Set N=2m+1>=3, d=2m, q=exp(pi i/N), Q=q^2, x=q^d,
F_a=(Q;Q)_a and s_a=|F_a|. All indices are unwrapped. Original
normalizations are those of the [full vertex kernel](actual_trivalent_complete_circle_vertex_kernel.md).

## 1. Actual source coefficient and exact positive evaluation

For 0<=j<=m put t=d-j. In the ORIGINAL physical pair define

    h^(j)_a=q^(a^2)[t choose a]_Q at |a,t-a>,
    W^(j)_r=F_pair^r h^(j)/F_r, 0<=r<=2j.             (1)

The highest equation follows from the ratio
-x^-1 Q^a(1-Q^(t-a))/(1-Q^(a+1)). Its Casimir is
c_j=q^(2j+1)+q^(-2j-1). At physical degree d,

    W^(j)_j(a,d-a)=q^(-j^2) f_a(c_j).                (2)

Indeed both sides solve the same actual tridiagonal eigenvector
recurrence, and the first entry of the coproduct binomial is
N x^-j/(F_t F_j)=q^(-j^2). No inverse frame is used.

Extract the black source rows (W^(m)_d,W^(j)_j,W^(m)_0), after
the literal port exchanges of the full kernel. Their pair degrees
are (3m,2m,m), summing to 3d. The actual coefficient is N^3 B_(N,j),
where

    B_(N,j)=sum_(k=0)^m x^(k-d)
        conjugate[(h^(m)_k)^2 W^(j)_j(m+k,m-k)].      (3)

Here the exact lowest-column identity W^(m)_d(m+k,d-k)=h^(m)_k
was proved with all phases in the [central anchor](actual_trivalent_steinberg_central_anchor.md#2-exact-source-normalizations-including-both-ends).
Thus (3) is an original source coefficient, not a chosen abstract 6j.
Define

    z_j(k)=s_(j+k)/[s_(j-k)s_k^2], 0<=k<=j,
    z_m(k)=beta(m,k)^2=N/[s_k^2 s_(m-k)^2].

The exact all-node formula is

    B_(N,j)=q^[m(2-3m+2j)] P_(N,j),
    P_(N,j)=sum_(k=0)^j z_j(k)z_m(k)>0.               (4)

It includes j=0,m, every odd composite N, and recovers the central
quartic at j=m. In the specified CD basis sqrt(N)W on the two
central legs and sqrt(2N)f(c_j) on the middle leg, j<m, the coefficient
is sqrt(2)N^(9/2)q^(-j^2)B_(N,j). At j=m it is N^(9/2)B_(N,m).
The sqrt(2) is the actual double-node FIRST-normal multiplicity;
one must not continue it through the odd simple node.

## 2. Own finite proof at every node

Let J_0 denote the actual complete anti-Pascal recoupling, not the
six-head cup. The [central proof](actual_trivalent_steinberg_central_anchor.md#4-a-finite-coherent-quartic-transform)
established by finite binomial inversion

    (J_0)_(a,b)=x D_aD_b[a+b choose a]_(Q^-1),
    D_a=(-q^-1)^a, a+b<=d; zero otherwise,
    conjugate(J_0) P J_0=P.                           (5)

The actual other Casimir is lower bidiagonal, with diagonal c_a and
lower entry Q^a+Q^-a-2. Hence y_j=J_0 f(c_j) is REAL, supported
at d-j,...,d, with

    (y_j)_(d-j+k)
      =s_(d-j)s_j/[s_(d-2j+k)s_k s_(j-k)^2].         (6)

Its last entry is (J_0)_(d,0)=1. Solve the first-order recurrence
backwards from there using

    (c_a-c_j)/[-(Q^a+Q^-a-2)]
     =-q^-1(1-Q^(a-j))(1-Q^(a+j+1))/(1-Q^a)^2.

The second occurrence of c_j forces all earlier entries to zero.
Root reflection F_aF_(d-a)=N(-1)^a Q^[a(a+1)/2] cancels every
phase in (6). Reversal P y_j is exactly the vector z_j above.

At this root z_j(i)=(-q)^i(Q^-j;Q)_i(Q^(j+1);Q)_i/F_i^2.
For k<=j form C_(j,k)=sum_(i=k)^j z_j(i)D_i[i choose k]_(Q^-1).
With n=j-k, its k-th term times the remaining series is

    (Q^-j;Q)_k(Q^(j+1);Q)_k/F_k^2
     *sum_(r=0)^n (Q^-n;Q)_r(Q^(j+k+1);Q)_r Q^(-kr)
                    /[F_r(Q^(k+1);Q)_r].

The SECOND finite q-Chu applies: b=Q^(j+k+1), c=Q^(k+1), and
cQ^n/b=Q^-k. It is the own finite identity obtained from the first
q-Chu at base Q^-1 by inverting parameters, as in the central proof.
All denominator indices are <=j<N. Its product side simplifies to

    C_(j,k)=(-1)^j q^[k^2-j(j+1)]z_j(k).             (7)

Vandermonde in (5) now gives, for ANY j,l<=m,

    z_j^T J_0 z_l=x(-1)^(j+l)q^[-j(j+1)-l(l+1)]
                  *sum_(k=0)^min(j,l)z_j(k)z_l(k).   (8)

To recover the actual source, (2),(3) and the phases of h^(m) give
B_(N,j)=q^[j^2-4m^2] f(c_j)^dagger J_0 f(c_m).
Since y_j,y_m are real, (5) rewrites this matrix element as
z_j^T J_0 z_m. Equation (8) and q^N=-1 give precisely (4).
This evaluates the coherent source BEFORE any absolute values.

## 3. Entire physical color bound and strict complement gap

For k<=j<m,

    z_(j+1)(k)/z_j(k)
      =sin[pi(j+k+1)/N]/sin[pi(j-k+1)/N]>=1.          (9)

For k>0 the difference of these sines is
2cos[pi(j+1)/N]sin(pi k/N)>0. Therefore

    1=P_(N,0)<=P_(N,j)<=P_(N,m),
    log P_(N,j)<=N j0+O(log N), j0=v8/pi.            (10)

For EVERY fixed delta>0 there is gamma_delta>0 such that

    max_(m-j>=delta N) P_(N,j)
                 <=poly(N)exp[N(j0-gamma_delta)].    (11)

Outside a fixed neighborhood of k/N=1/4 the central quartic terms
already have a strict gap. Inside it, sum log(9) over a fixed
subinterval between j/N and 1/2. Its continuous positive integral
is uniformly bounded below when (m-j)/N>=delta. The uniform
O(log N) sine-factorial estimate covers endpoints. This proves
(11), with an empty physical range simply ignored.

## 4. Exact complex-color factorial packet

Let S_hat_N be the [canonical sine factorial](exact_factorial_interpolation_and_complex_contours.md),
with S_hat_N(a)=s_a and S_hat_N(z)S_hat_N(d-z)=N EXACTLY.
Fix a small epsilon>0, I_N={k:|k/N-1/4|<=epsilon}, and set

    Pwin_N(sigma)=N sum_(k in I_N)
      S_hat_N(m-Nsigma+k)
       /[S_hat_N(m-Nsigma-k)s_k^4s_(m-k)^2].          (12)

This is an EXACT holomorphic function on a fixed small complex
sigma disk, with all scaled factorial arguments in a compact bulk
strip. It is EXACTLY EVEN by reflection. At physical sigma=(m-j)/N
it is exactly the retained terms of (4). Their omitted positive terms
have a uniform exponential gap, also relative to the retained packet
after shrinking the disk. The original source completion is
q^[m(2-m)-2mN sigma]Pwin_N(sigma); at integral deficit s its extra
character is (-1)^s q^s, which has NOT been deleted.

Put J(t)=integral_0^t Log(2sin pi a)da on the marked bulk strip and

    F(t,sigma)=J(1/2-sigma+t)-J(1/2-sigma-t)
                                -4J(t)-2J(1/2-t).    (13)

The canonical complex factorial expansion, including the actual
half-step m/N=1/2-1/(2N), gives the summand in (12) as

    exp[NF(t,sigma)]/[4N^2 sin^2(pi t)] *[1+O(1/N)], (14)

uniformly on a slightly larger complex t,sigma tube. The square
root of the numerator/denominator sine ratio cancels the phase
shift exp[-(G(1/2-sigma+t)-G(1/2-sigma-t))/2], G=J'.
The remaining exp[G(1/2-t)]=2cos(pi t) cancels its denominator.
Thus (14) has neither an unknown periodic multiplier nor a missing
half-step constant.

The unique real saddle continues holomorphically as

    t_*(sigma)=atan(cos pi sigma)/pi,
    A(sigma)=-F_tt(t_*,sigma)
             =2pi[1+cos^2(pi sigma)]^2/cos^3(pi sigma).

For real small sigma, strict concavity follows directly from the
cotangent derivatives in (13). Let Phi(sigma)=F(t_*,sigma). Then

    Phi(0)=j0, Phi'(sigma)=-2 artanh(sin pi sigma),
    Phi''(sigma)=-2pi/cos pi sigma,
    Phi(sigma)=j0-pi sigma^2+O(sigma^4).              (15)

The EXACT packet has the uniform COMPLEX asymptotic

    Pwin_N(sigma)=N^(-3/2) exp[NPhi(sigma)]
            /[4sqrt(cos pi sigma)] *[1+O(1/N)].      (16)

Here sqrt is +1 at zero. For completeness, enclose I_N by half-grid
vertical sides and horizontal sides of fixed small height b, using
the exact kernel pi N cot(pi N t). The vertical sides have |cot|<=1
and retain the source endpoint currents; their phase has a strict
window boundary gap. On horizontal sides the cotangent error is
O(exp(-2pi N b)), whereas phase growth is <=Cb^2+C|sigma|^2b.
Choose b first with Cb^2<pi b and then shrink the complex sigma disk.
All these errors and the endpoint connectors are exponentially
gapped. The main contours deform through t_* within the same
zero-free factorial strip. Analytic Gaussian integration of (14)
gives (16), since sqrt(2pi/A)/(4sin^2(pi t_*))=1/[4sqrt(cos pi sigma)].
This proves uniformity for the exact packet, not just its real-grid
leading terms. Cauchy estimates keep every FIXED color derivative.
In particular on smaller real/imaginary corridors,

    |Pwin_N(x+iy)|<=poly(N)exp[N(j0-cx^2+Cy^2)], c>0. (17)

## 5. Remaining branching interfaces

The theorem concerns a genuine original black coefficient with two
central legs. The double-node CD factor above has retained the first
normal of the complete circle BEFORE its fixed-root image is taken.
Equation (12) continues color in this coefficient; it does NOT take
derivatives of a moving-q physical source germ.
Here sigma is an INTERNAL pair-Casimir channel deficit. It has not
been identified with an auxiliary meridian or an ordinary-circle
color parameter; such an identification needs its own actual source
and peripheral transport certificate.

For three independently noncentral legs the actual kernel still has
three distinct highest/descendant polynomials. The reduction to (8)
used the two central legs essentially. One magnetic coefficient also
does not bound all other T_i, or identify the distinct U,V,V_m.
Paired socle columns have W^dagger P W=0, whereas the central column
has W^dagger P W=I; its retraction cannot simply be continued.
Those remain explicit interfaces before an arbitrary noncrossing
triple-partition graph can be estimated by this positive packet.

Audit: [literal source and all-node finite transform](../experiments/audit_actual_trivalent_one_channel_source_packet.py).
Tests supplement the finite proof and contour estimate; no sewn-graph
survival or new hyperbolic-volume claim is inferred from them.

Independent internal analytical review passed the all-node finite
transform, actual source phase, entire-color gap, half-step amplitude
and exact complex-window contour argument. A fresh primary replay
passed ten original all-node families N=3,...,21, three whole-color
Laplace profiles and two canonical complex factorial windows.
