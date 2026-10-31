# An exact original trivalent beta cycle and its norm remainder

28 October 2026. The original balanced head equation at a trivalent
vertex now has a specified one-dimensional relative source. Its
finite convolution is an explicit Newton polynomial. A norm-corrected
Barnes contour splits this polynomial into a NONZERO balanced residue
block and an explicitly retained normalization term. The Barnes factor
of that latter term is uniformly bounded on compact positive boundary
families. No unknown knot coefficient or replaced invariant occurs.

This is a local source theorem. The norm factor can have exponential
size; the rate of the nonzero residue block and its comparison with
that normalization term are separate. Nonvanishing of this block does
not yet prove the global knot period selects it after all other
boundary integrations.

## 1. The source and its exact finite polynomial

Use the original full functions Psi_+, Psi_- from
[the circle-and-boundary source theorem](actual_modular_dilog_circle_and_boundary_source.md).
Put N>=2, d=N-1, h=2*pi*i/N and Q=exp h. Their coefficients through
degree d are

    p_a=(-1)^a Q^(a(a-1)/2)/(Q;Q)_a,
    m_a=Q^a/(Q;Q)_a.

After the exact reflection of the positive factorial order, the
trivalent fiber field is precisely

    F_N(L;U,V)=r^d Psi_-(Log U-L)
                        Psi_+(Log V-L)Psi_+(-L), r=exp L.  (1)

The graph incidence argument in
[the bipyramid source note](positive_bipyramid_source_transport.md#4-the-original-source-law-checked-on-the-actual-reduced-graph)
shows that its constant Laurent coefficient is the original complete
source convolution, with all original boundary tags retained. The
finite q-binomial calculation gives

    [r^0] F_N=(Q^(-d)/N) B_N(Q^2 U,Q V),
    B_N(u,v)=sum_(a=0)^d product_(j=0)^(a-1)(u-Q^j v). (2)

The empty product is one. Thus u=Q^2 U, v=Q V and N Q^d are exact
tags and normalization, not only their classical limits.

The basic original-source recurrences are

    B_N(u,v)=(u-v)B_N(u,Qv)+D_N(u,v),
    v B_N(Qu,Qv)=(u-1)B_N(u,v)+D_N(u,v),
    D_N(u,v)=1-u^N+v^N.                              (3)

The second follows by summing
Q^a p_a=(u p_a-p_(a+1))/v for the Newton products p_a.
Both endpoint terms are part of the source.

## 2. A single exact outer-Hankel current

At large r, each full Psi in (1) has its first N ordinary coefficients
plus O_N((1+|Log r|)|r|^(-N)). Therefore F_N is its ordinary Laurent
polynomial down through the constant term plus O_N(log|r|/|r|),
uniformly over a bounded logarithmic turn. Its generalized constant
coefficient is consequently an actual limit of full lifted circles.

Write

    M_N(r)=(r^N-V^N)(r^N-1)/[r^N(r^N-U^N)],
    C_N(R)=(1/(2*pi*i)) integral_(log R-i*pi)^(log R+i*pi)
                                                    F_N(L)dL.

For R initially larger than max(1,|U|,|V|), with the fixed logarithmic
marks in (1), the EXACT source identity is

    [r^0]F_N=C_N(R)+(1/(2*pi*i)) integral_R^infinity
          [M_N(-s)-1]F_N(log s-i*pi) ds/s.              (4)

Indeed F_N(L+2*pi*i)=M_N(exp L)F_N(L). Apply Cauchy's theorem
to the logarithmic rectangle log R<=Re L<=log S and let S increase
to infinity. The circle's positive Laurent powers integrate to zero,
and its remainder tends to zero. The outer integral converges because
M_N(-s)-1=O_N(s^(-N)) and d=N-1. This identity is the simultaneous
pushforward of the coefficient source. It carries all mixed original
radial pieces; it is not a replacement by three bare circles.

Subsequent contour continuation retains the poles and end faces it
crosses. No unproved positive separating contour is assigned to (4).

## 3. A convergent Barnes contour with a variable central norm

Consider the positive boundary chamber

    Im u<0, Im(v/u)>0.                               (5)

Fix Log u with -pi<Arg u<0 and c=Log(v/u) with 0<Im c<pi.
Their sum is the continuous logarithm of v, whose imaginary part
lies strictly between -pi and pi. Choose 0<epsilon<1 with
2*pi*epsilon/N<Im c. Define

    g(a)=exp(a Log u) Psi_+(c)/Psi_+(c+h a),
    t=exp(2*pi*i*a), lambda(t)=u^N-v^N t,
    I_N(u,v)=integral_(-epsilon-i*infinity)^(-epsilon+i*infinity)
                                     g(a)/(exp(-2*pi*i*a)-1) da. (6)

The line is oriented UPWARD. The exact full-Psi steps give

    g(n)=product_(j<n)(u-Q^j v),
    g(a+N)=[u^N-v^N exp(2*pi*i*a)]g(a).               (7)

The variable exponential in (7) is essential. A constant Floquet
multiplier is true at integer samples only, and cannot be used in
a complex contour argument.

On the entire strip -epsilon<=Re a<=N-epsilon, the denominator
Psi_+(c+h a) has no zeros: its argument has positive imaginary
part, whereas the zeros of Psi_+ occur at nonpositive imaginary
integer combinations of h and 2*pi*i. Thus g is holomorphic there.

## 4. Exact norm-pole residue transport

Assume temporarily u^N!=1 and D_N!=0, and choose alpha with

    exp(2*pi*i*alpha)=(u^N-1)/v^N,
    -epsilon<Re alpha<1-epsilon,
    v_*=v exp(h alpha), so u^N-v_*^N=1.              (8)

Avoid parameters with a pole on the two chosen vertical sides;
the result extends by continuation. Use the original sample-preserving
norm-corrected differential

    omega=2*pi*i D_N t g(a)
                        da/[(t-1)(1-lambda(t))].        (9)

Its residues are g(n) at n=0,...,N-1 and -g(alpha+k) at
alpha+k, k=0,...,N-1. At the latter points

    g(alpha+k)=g(alpha) product_(j<k)(u-Q^j v_*).

The factor t in (9) is important BOTH for these residues and for
the ends. For Im a tending to positive infinity it supplies the
decay exp(-2*pi Im a). For Im a tending to negative infinity, the
two denominator factors and this numerator leave the decay
exp(-2*pi |Im a|), overcoming the full right-edge growth of g.
The full-Phi horizontal asymptotics prove that the horizontal sides
of the width-N rectangle tend to zero, uniformly in its real coordinate.

On its two vertical sides, (7) gives

    omega(a+N)-omega(a)
             =2*pi*i D_N g(a)/(exp(-2*pi*i*a)-1) da.

The residue theorem therefore proves the exact source-cycle identity

    B_N(u,v)=S_N(u,v)+D_N(u,v) I_N(u,v),
    S_N(u,v)=g(alpha) B_N(u,v_*).                       (10)

All central norm factors are retained. The extra norm poles are not
discarded: their complete balanced Fourier block is the first term.
Changing alpha by an integer does not change S_N, by the balanced
version of (3). Thus (10) is independent of the root/deck choice.

The balanced block B_N(u,v_*) is nonzero if uv_*!=0. One elementary
proof takes the discrete Fourier transform of the cyclic sequence
p_k=product_(j<k)(u-Q^jv_*), for which p_N=p_0=1. Its Fourier
components obey a first-order cyclic recurrence with all coefficients
nonzero. No component, including their zero-frequency sum B_N, can
vanish. This is a finite source statement, not an asymptotic argument.
The other factors in S_N are nonzero in the stated chamber.

At D_N=0, equation (10) extends directly and S_N=B_N is nonzero.
At u^N=1 the norm pole escapes and must be checked separately.
If u_0=Q^(-j) with its lower principal argument, the first nonzero
coefficient of B_N(u_0,w) is b_j w^j, b_j!=0. This follows from

    (u_0 Q^k-1)b_k=Q^(k-1)b_(k-1)

and its nonzero top coefficient. As u tends to u_0, v_*^j contributes
[(u^N-1)/v^N]^(j/N), exactly cancelling the opposite power in
exp(alpha Log u). Since Psi_+(c+h alpha) tends to one, the finite
limit is Psi_+(c)b_j v^j!=0. This is a fixed-N collision calculation;
no uniform collision asymptotic is assumed. Consequently S_N is
nonzero throughout (5), after these specified removable continuations.

## 5. The Barnes normalization term is uniformly tame

For every compact K inside (5), there are C_K and N_K such that

    |I_N(u,v)|<=C_K, (u,v) in K, N>=N_K.              (11)

This bound includes the norm collisions just described. To prove it,
write a=-epsilon+i N y and x=v/u. The uniform actual full-Psi
symbol on the entire selected strip gives the leading real exponent

    R_N(y)=-y Arg u+
       Im[Li_2(x)-Li_2(x exp(-2*pi*i*epsilon/N-2*pi*y))]/(2*pi).

Here N R_N(0)=O_K(1). Its EXACT leading derivative is

    R_N'(y)=-Arg u-
           Arg(1-x exp(-2*pi*i*epsilon/N-2*pi*y)).       (12)

It lies between -Arg u>0 and pi-Arg v+O_K(1/N)<2*pi.
Thus R_N(y)<=O_K(1/N)+eta y for y<=0, while
R_N(y)-2*pi*y<=O_K(1/N)-eta y for y>=0, with a fixed
eta>0. The denominator in (6) supplies precisely exp(-2*pi*N*y)
on the positive half-line and is bounded on the negative half-line.
The full-Psi amplitude ratio is bounded uniformly for all real y,
because its selected argument stays a fixed distance from the
positive real ray. Its relative error is O_K(1/N).

The resulting integrand is bounded by C_K exp(-eta |Im a|).
This proves (11); the apparent N in da=N i dy cancels its
decay scale N^(-1). A fixed finite set of smaller N is treated by
the original horizontal full-Phi bounds.

The leading normalization symbol can also be determined rather than
left unspecified. Uniformly on the same compact families,

    I_N=1/(1-u+v)-h*v*(u-v)/(1-u+v)^3+O_K(h^2).        (11a)

For a on the fixed vertical line with |Im a|<=C log N, the actual
full-Psi symbol and its holomorphic derivative bound give

    g(a)=(u-v)^a [1-h*a*(a-1)*(v/u)/(2*(1-v/u))
                                      +O_K(h^2*(1+|a|^6))].

Here Log(u-v)=Log u+Log(1-v/u) has imaginary part in (-2*pi,0).
The exponentially decaying tails proved above permit a cutoff C log N
with error smaller than any fixed inverse power, while the displayed
error integrates to O(h^2). The elementary convergent Barnes identity

    integral_(Re a=-epsilon,up) w^a/(exp(-2*pi*i*a)-1) da
                                                    =1/(1-w)

holds on that cut plane, first by closing to the right for |w|<1
and then by analytic continuation. Applying w^2*d_w^2 proves (11a).
The same coefficient also follows from the exact current recurrence
I_N(u,v)=(u-v)I_N(u,Qv)+1 on their common logarithmic chamber.
Thus the retained term is three explicit norm phases 1,u^N,v^N
times an analytic normalization symbol. This asymptotic description
does not discard possible subdominant exponentially small pieces.

The normalization group's rate therefore obeys

    limsup (1/N) log |D_N I_N|
                         <=max(0,log|u|,log|v|),        (13)

uniformly on compact families. It is NOT always exponentially small.
For instance it can have the original boundary norm rate. Any proof
of a geometric lower bound must compare S_N with this retained term
and with the subsequent exterior source; it cannot discard (13).

## 6. The actual homogeneous source line, with its normalizer explicit

The zero-charge part now really is an explicit torsor section.
Put c_*=c+h alpha, so exp(N c_*)=1-u^(-N). Equation (10) becomes

    S_N(u,v)=A_N(u) exp[-c Log u/h] Psi_+(c),
    A_N(u)=exp[c_* Log u/h] B_N(u,u exp c_*)/Psi_+(c_*). (14)

Changing c_* by h leaves A_N unchanged by (3) and the full-Psi
shift. Thus A_N depends only on u and is NONZERO; there is no
unidentified knot scalar in this local source formula.

On a common lower logarithmic chamber (and subsequently by the
specified analytic continuation), the exact source equations imply

    A_N(Qu)=(1-u^(-1))A_N(u).                         (15)

The selected function Psi_+(h-Log u) has the same step. Their quotient
is h-periodic in Log u. This observation alone does NOT make that
quotient constant or tame. The subsequent
[exact normalizer proof](actual_trivalent_beta_normalizer.md) uses
the actual source's divisor and both end bounds to determine it:

    A_N(u)=(N/phi_N) u^N Psi_+(h-Log u).                (15a)

The central u^N is compulsory and may have an exponential rate.
Periodicity by itself would not have justified its omission.

The classical growing saddle of the original fiber is
r=V/(1+V-U), and its signed positive bipyramid has
V/r and 1/r upper and U/r lower. The exact nonzero section (14)
is the candidate that can carry this growing block. Its comparison
with the full geometric normal contour and the bound (13) remains
the next step. The earlier charged REAL kernel with negative volume
rate is not used as a substitute for this original source.

## 7. Positive geometry alone does not dominate this local source

There is a useful exact obstruction to dropping the norm-gap or the
exterior boundary functional. Whenever |u|+|v|<=c<1,

    |B_N(u,v)|<=1/(1-c),
    B_N(u,v) -> 1/(1-u+v) as N -> infinity.              (16)

Every Newton product is bounded by c^a. For each fixed a it tends
to (u-v)^a as Q tends to one, so dominated convergence proves both
claims. This is an open chamber of the original polynomial source.

It contains genuine strictly positive signed bipyramids. For example
take u=-4*i/5 and v=1/100. The three-side shapes and two outputs are

    p=1+v-u=101/100+4*i/5,
    q=p/v=101+80*i,
    H=u*q=64-404*i/5,
    p/H=v/u=i/80, q/H=1/u=5*i/4.

Both p,q are upper, H is lower, and both outputs are upper; their
oriented volume D(p)+D(q)-D(H)=D(i/80)+D(5*i/4) is strictly positive.
Nevertheless the actual local source (16) has rate ZERO. The exact
original tags in (2) converge to these same shapes, so this is not
a replacement by a different quantum atom.

Thus a positive classical bipyramid cannot by itself force the
scalar trivalent source to grow at its volume. Its boundary Legendre
terms, branch marks and the complete exterior pairing matter.
In a family where the explicit residue rate DOES strictly exceed
max(0,log|u|,log|v|), (10)--(13) instead give B_N=S_N(1+o(1))
with an exponentially small relative remainder, once the residue's
uniform logarithmic error is controlled. The present note proves the
exact source decomposition and remainder bound; it does not assume
that inequality for every positive bipyramid or every knot network.
