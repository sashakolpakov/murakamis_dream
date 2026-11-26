# The partial endpoint Green estimate and its retained boundary packet

Private written proof, 16 November 2026.

The exact truncation defect has the real product rate, uniformly even
at its zeros. Backward propagation on a fixed physical bulk interval
preserves that rate for the forced part of the error, including first
normals. The estimate also retains an off-grid boundary packet and the
defect of the chosen baseline. Neither of those terms is identified
with the last Newton product.

An exact ideal-multiple example shows why matching physical jets and
thin-strip moderateness do not determine the error. This is not an
obstruction to a sharper estimate for the specifically normalized
common baseline, and does not provide a filled-leaf scalar seed.

## 1. The ordinary truncation and its physical window

Put
\[
 h=N^{-1},\quad \theta=\pi/N,\quad D=N-1,\quad
 c_a=2\cos((2a+1)\theta),\quad s_a=2\sin(a\theta),
\]
\[
 S_k=\prod_{a=1}^k s_a,\qquad
 e_k(C)=S_k^{-2}\prod_{a<k}(c_a-C),\qquad
 w=2\cosh(\alpha/N),
\]
\[
 c_N(x)=2\cos(2\pi x+\pi h),\quad
 t_N(x)=\pi-2\pi x-\pi h,\quad k_0=\lceil N/2\rceil.
 \tag{1}
\]
The parameter \(\alpha\) ranges over an arbitrary fixed bounded
complex disk; larger disks are used for derivatives. Fix
\(0<\delta<1/2\), let \(L=\lfloor\delta N\rfloor\),
\(K=k_0+L<D\) for large \(N\), and define
\[
 H_K(C)=\sum_{a=0}^K e_a(w)e_a(C),\qquad
                       u_N(x)=H_K(c_N(x)).                  \tag{2}
\]
The ordinary original operator, denoted by \(\mathscr J_N\) on
functions of \(x\), is
\[
 \mathscr J_N F=(c_0+A_N+B_N)F-A_NF(x+h)-B_NF(x-h),
\]
\[
 A_N(x)=\frac{s_{Nx+1}^4}{s_{2Nx+1}s_{2Nx+2}},\qquad
 B_N(x)=\frac{s_{Nx}^4}{s_{2Nx}s_{2Nx+1}}.                  \tag{3}
\]
On polynomials in \(C\) it is the ordinary lift of \(J=TCT\),
with lowering rule \(Je_a=c_ae_a-s_a^2e_{a-1}\). Therefore
\[
 \boxed{\quad
 R_N(x):=(\mathscr J_N-w)u_N(x)
     =s_{K+1}^2e_{K+1}(w)e_K(c_N(x)).
 \quad}                                                     \tag{4}
\]
Indeed \((c_a-w)e_a(w)=s_{a+1}^2e_{a+1}(w)\), so every
coefficient except the last cancels in the finite sum. Equation
(4) is ordinary, before any quotient reduction or differentiation.

Fix a closed interval \(I=[a,b]\) with a larger fixed real buffer
inside \((0,1/2)\), such that throughout that buffer, for large
\(N\),
\[
                  0<t_-\le t_N(x)\le t_+<2\pi\delta.       \tag{5}
\]
At every physical node \(x=j/N\) in this window, \(H_K\) and
the full kernel \(K_N(w,C)\) have exactly the same value and
first spectral normal. The omitted Newton terms contain both
occurrences of each such physical root. This also follows from
the exact physical termination in the scalar-compatibility source.
The window is strictly in the bulk, so no extra spectral normal
is introduced at an odd simple endpoint.

## 2. A uniform product estimate, including its zeros

Define the continuous real rate
\[
 J_\delta(t)=-\int_0^\delta
       \log\left|\frac{\sin^2(t/2)-\sin^2(\pi v)}
                         {\cos^2(\pi v)}\right|\,dv .       \tag{6}
\]
The logarithmic singularity is integrable. On (5), for every
fixed pair of nonnegative derivative orders \(a_1,b_1\),
\[
 \boxed{\quad
 |\partial_\alpha^{a_1}\partial_x^{b_1}R_N(x)|
           \le C N^p e^{-N J_\delta(t_N(x))},\qquad x\in I.
 \quad}                                                     \tag{7}
\]
The constants can depend on the interval, cutoff and derivative
orders. The estimate is uniform at product zeros and at both level
parities. It is an upper bound, not a nonzero product asymptotic.

Here is a proof with the needed zero control. Let \(Q_N\) be the
monic distinct-node polynomial. The exact product formulas give
\[
 R_N=(c_K-w)\beta_N Q_N(c_N(x))
                         \prod_{l=0}^{L-1}\rho_{l,N},       \tag{8}
\]
where
\[
 \rho_{l,N}(\alpha,t)=
 \frac{[\cos^2 A_l+\sinh^2(\alpha/(2N))]
             [\sin^2(t/2)-\sin^2 A_l]}{\cos^4 B_l},
\]
\[
 (A_l,B_l)=
 \begin{cases}
 ((l+\tfrac12)\theta,(l+1)\theta),&N\text{ even},\\
 ((l+1)\theta,(l+\tfrac32)\theta),&N\text{ odd},
 \end{cases}
\]
\[
 \beta_N=
 \begin{cases}
 \cosh(\alpha/2)/(2N^2),&N\text{ even},\\
 \cosh(\alpha/2)\cosh(\alpha/(2N))
                   /(4N^2\cos^4(\theta/2)),&N\text{ odd}.
 \end{cases}                                                \tag{9}
\]
On every disk \(|z-x|\le r/N\), with fixed \(r\), the factors
\(c_K-w\), \(N^2\beta_N\), and \(Q_N(c_N(z))\) are bounded.
For the last assertion use
\(Q_N(c_N(z))=-a_N(z)\sin(\pi Nz)\), with
\(a_N=2\) at even levels and
\(a_N=4\cos(\pi z+\pi/(2N))\) at odd levels.

The cosine factors in (9) are uniform units. Their logarithmic
sums are smooth Riemann sums; the microscopic parameter changes
their logarithm by \(O(N^{-1})\) in total. For the numerator use
\[
 \sin^2(t/2)-\sin^2 A_l
                   =\sin(t/2+A_l)\sin(t/2-A_l).             \tag{10}
\]
The first sine is a uniform unit on the buffered real window.
In the second, write \(\sin y=y(\sin y/y)\). Its second factor
is a uniform analytic unit. The remaining product has, up to
\((\pi/N)^L\), the form
\(\prod_{l<L}(\xi-l-\omega)\), where
\(\Re\xi\) is a distance \(cN\) from both ends of the index
interval and \(|\Im\xi|+|\omega|\) is bounded. Splitting at the
nearest integer and comparing the two sides with
\(\prod_{k\le m}(k+C)\) bounds this product by the corresponding
two factorials times a fixed power of \(N\). Stirling's elementary
logarithmic estimate gives
\[
 \log\left|\prod_{l<L}\rho_{l,N}(\alpha,t_N(z))\right|
       \le -N J_\delta(t_N(x))+C\log N,
                     \qquad |z-x|\le r/N.                  \tag{11}
\]
The bounded shifts and the floor in \(L\) change the estimate
by \(O(\log N)\). A factor arbitrarily near zero can only improve
this upper estimate; no lower bound on its distance from zero
was used. The factorial comparison also covers complex distances
of size \(O(N^{-1})\) from the real zero. This proves (11)
uniformly on the indicated disks. Combining it with (8), then
using Cauchy's formula on smaller disks and larger parameter
disks, proves (7). In particular fixed \(x\)-derivatives cost
only additional powers of \(N\).

On the window (5), direct differentiation gives
\[
 J_\delta'(t)=-\frac1{2\pi}
     \log\frac{\tan(\pi\delta)+\tan(t/2)}
                   {\tan(\pi\delta)-\tan(t/2)}<0.           \tag{12}
\]
One obtains (12) by substituting \(y=\tan(\pi v)\) in the
principal-value integral for the derivative of (6). All arguments
in the displayed logarithm are positive because \(t<2\pi\delta\).
Also \(J_\delta(t)>0\) there: at \(t=2\pi\delta\), every
nonzero ratio inside (6) is less than one, and (12) increases
the rate as \(t\) decreases. Thus
\(J_\delta(t_N(x))\) is increasing with \(x\).

## 3. Exact backward Green propagation with first normals

Let \(H_N(x,\alpha)\) be any holomorphic baseline on the buffered
bulk neighborhood, and retain its actual ordinary defect
\[
                r_H=(\mathscr J_N-w)H_N,\qquad E_N=u_N-H_N.
 \tag{13}
\]
No bound or normalization of \(H_N\) is implicit here. For a
holomorphic scalar \(F\), define
\[
 X_F(x)=\binom{F(x)}{N(F(x)-F(x-h))},\qquad
 Z_F(x)=\binom{X_F(x)}{\partial_xX_F(x)}.                    \tag{14}
\]
Primes below differentiate the ordinary coefficient functions.
Put
\[
 q_N=B_N/A_N,\quad d_N=(c_0-w)/A_N,\quad
 T_N=\begin{pmatrix}1+d_N&q_N/N\\Nd_N&q_N\end{pmatrix},
\]
\[
 b_N=A_N^{-1}\binom1N,\qquad
 \mathcal T_N=\begin{pmatrix}T_N&0\\T_N'&T_N\end{pmatrix},
 \qquad
 \mathcal R_N(r)=\binom{b_Nr}{b_N'r+b_Nr'}.                 \tag{15}
\]
Solving (3) for the forward value and differentiating gives exactly
\[
 Z_F(x+h)=\mathcal T_N(x)Z_F(x)
                 -\mathcal R_N((\mathscr J_N-w)F)(x).
 \tag{16}
\]
This includes coefficient derivatives and the independent normal
state. It does not infer a normal equation from values alone.

On the fixed buffered bulk domain,
\[
 A_N=\tan^2(\pi x)+O(h),\quad q_N=1+O(h),\quad
 d_N=O(h^2),\quad T_N=I+O(h),\quad T_N'=O(h).
 \tag{17}
\]
These follow directly from (3), uniformly for bounded complex
\(\alpha\); the same estimates hold on a fixed smaller complex
neighborhood. In particular
\(\mathcal T_N^{\pm1}=I+O(h)\), and
\[
              \|\mathcal R_N(r)\|
                       \le CN(|r|+|r'|).                   \tag{18}
\]

Choose any fractional grid \(x_j=(j+\vartheta)/N\),
\(0\le\vartheta<1\), and indices \(j\le b_N^*\) with their
row points in \(I\) and all neighboring arguments inside its
buffer. The symbol
\(b_N^*\) is an index, distinct from the vector \(b_N\) in (15).
Let \(\Phi_{j,k}\) be the fundamental propagator of (16)'s
homogeneous matrix, with \(\Phi_{k,k}=I\), and use inverse
products when \(j<k\). Uniformly on this fixed real interval,
\[
                         \|\Phi_{j,k}\|\le C.              \tag{19}
\]
Indeed there are at most \(CN\) factors of norm \(1+Ch\).

Backward variation of constants is the ordinary exact identity
\[
 \boxed{\quad
 Z_{E_N}(x_j)=\Phi_{j,b_N^*}Z_{E_N}(x_{b_N^*})
   +\sum_{l=j}^{b_N^*-1}\Phi_{j,l+1}
                   \mathcal R_N(R_N-r_H)(x_l).
 \quad}                                                     \tag{20}
\]
In particular (7), (12), and (18)--(19) give
\[
 \boxed{\quad
 \|Z_{E_N}(x_j)\|
 \le C\|Z_{E_N}(x_{b_N^*})\|
       +CN^p e^{-N J_\delta(t_N(x_j))}
       +CN\sum_{l=j}^{b_N^*-1}(|r_H(x_l)|+|r_H'(x_l)|).
 \quad}                                                     \tag{21}
\]
The right boundary packet contains both adjacent scalar values
and both adjacent first derivatives, as encoded in (14).
It is actual data for the same fractional grid. It is not replaced
by a packet on the physical grid or by an incoming rate at the
left boundary. All constants are uniform in \(\vartheta\).

For an exact homogeneous baseline the last term is zero. For a
baseline whose defect and its first derivative are bounded by
\(N^p e^{-\kappa N}\), it is at most another polynomial times
\(e^{-\kappa N}\). Neither case deletes the boundary term.
Since \(c_N'\) is a uniform unit in this bulk, the same estimate
controls first spectral normals with the stated polynomial losses.
Parameter derivatives obey the analogous differentiated identity,
or Cauchy estimates when the supplied packets are uniformly
holomorphic on larger parameter sets.

In particular, for the specifically constructed baseline \(A_N^0\)
of the common-baseline source, the missing datum has the literal form
\[
 \mathfrak b_N^\delta(\vartheta)
       =Z_{u_N-A_N^0}(x_{b,N}(\vartheta)),\qquad
 x_{b,N}(\vartheta)=\frac{\lfloor Nb-\vartheta\rfloor+\vartheta}{N}.
 \tag{21a}
\]
At a specified target \(x_0\), choosing
\(\delta=\delta_*(\pi-2\pi x_0)\) leaves the concrete obligations
to bound (21a) and the last sum in (21) by a polynomial times
\(e^{-NJ_*(\pi-2\pi x_0)}\), uniformly in \(\vartheta\).
The \(O(N^{-1})\) angle offset changes this rate only by a bounded
factor on the fixed bulk arc. Initializing the modified differential
equation at a far-right physical row fixes its two-component state
at that row. It does not supply this sharper bound at the adjacent
fractional grids, or for the derivative part of (21a). The currently
proved exponential compatibility estimate has no such optimized
constant.

## 4. What changing the cutoff controls

Fix \(0<\delta_1<\delta_2<1/2\) and a real buffered arc with
\(0<t<2\pi\delta_1\). The two partial polynomials have the same
physical full jets on that arc. Their exact difference is the
finite Newton band between the two cutoffs. The product proof in
section 2 is uniform for every intermediate cutoff. For
\(\delta>t/(2\pi)\), the ratio
\[
                 \frac{\sin^2(\pi\delta)-\sin^2(t/2)}
                                      {\cos^2(\pi\delta)}
\]
increases from zero to infinity. Hence \(J_\delta(t)\), as a
function of \(\delta\), increases to its unique maximum and
then decreases. Its minimum on \([\delta_1,\delta_2]\) is at
an endpoint. Summing the \(O(N)\) exact terms and using the same
small disks proves, for every fixed derivative order,
\[
 |\partial_\alpha^{a_1}\partial_x^{b_1}
       (u_N^{\delta_2}-u_N^{\delta_1})(x)|
 \le CN^p\exp\{-N\min(J_{\delta_1}(t_N(x)),
                              J_{\delta_2}(t_N(x)))\}.      \tag{22}
\]
The maximizing cutoff satisfies
\(\sin^2(\pi\delta_*(t))=(1+\sin^2(t/2))/2\), giving the
previously proved \(J_*(t)\). Formula (22) bounds cutoff
variation. It does not bound the component common to these
partial polynomials relative to a separately normalized baseline.
In particular it does not identify the error in (21) with
\(e^{-NJ_*(t)}\).

## 5. An exact alias ambiguity and its limited implication

The full physical relation is
\[
 P_N(C)=2T_N(C/2)+2,\qquad
                 P_N(c_N(x))=4\sin^2(\pi Nx).              \tag{23}
\]
Its composition in (23) is \(h\)-periodic, so it commutes
with (3). Consequently
\(\mathscr J_N(P_NF)=P_N\mathscr J_NF\) as an ordinary
identity, with the removable polynomial interpretation.

At \(\alpha=i\pi\), one has \(w=c_0\), and the full kernel
and every partial polynomial in (2) are exactly \(1\).
For any fixed \(c>0\), however,
\[
             \widetilde H_N(x)
                 =1+e^{-cN}\sin^2(\pi Nx)                  \tag{24}
\]
is another exact homogeneous solution of
\((\mathscr J_N-c_0)\widetilde H_N=0\). It has exactly the
same full physical jets. In ordinary spectral terms the difference
is \(e^{-cN}P_N(C)/4\). It has zero first normal at every double
root and zero value at the odd simple root.

On every fixed bulk strip of height \(H<c/(2\pi)\), (24) is
uniformly bounded. At real midpoint rows its difference from
the partial polynomial is exactly \(e^{-cN}\), while the
truncation defect (4) is identically zero. Choosing
\(c<\min_{x\in I}J_\delta(t_N(x))\) for large \(N\) also
rules out a universal \(N^p e^{-NJ_\delta}\) comparison with
every such moderate homogeneous representative.

This example proves only that physical jets, thin-strip
moderateness, and the truncation forcing do not fix the off-grid
normalization. It does not contradict the specifically normalized
common baseline, nor exclude an improved boundary estimate for
that baseline on a larger domain. In fact its modified-flow
construction preserves the constant solution at \(\alpha=i\pi\):
the initial coefficient matrix kills \((1,0)^t\), and every flow
iteration retains that property. Thus (24) is not that constructed
baseline. In the original closed trace
the ideal multiple is invisible, with any shared polynomial
spectator and its full normals retained. Splitting that trace
into exterior and interface currents must keep their cancellation;
one separate current is not invariant under this ambiguity.

The unresolved estimate is therefore a source-specific bound on
the boundary packet and baseline defect in (21), at the required
action. Neither the optimized real product rate nor this Green
identity supplies that estimate or a nonzero filled-leaf term.

## 6. Coverage and direct sources

The ordinary finite truncation identity and its both-parity product
are prior results. The additional statement here is their uniform
real zero-inclusive forcing bound, the explicit backward full-normal
Green budget, and the normalization diagnostic. A targeted source
search found the earlier coarse holomorphic iteration and a lower
bound on its complex forcing, but no statement of (21).

The following complete sources were read at unchanged pins, with
their used implications checked:

* [Ordinary truncation and both-parity lowering product](research_endpoint_low_high_exponential_cancellation.md),
  SHA256 594bd802439d08e3dfe32f6cfa1027d291b36c502061dc7723fd0a8734527f5d.
* [Exact partial scalar and original physical jets](research_microscopic_endpoint_bulk_scalar_compatibility.md),
  SHA256 2b8713ed16b66f5faa004403ac1d032021eee0a6f8f38082481d002c672c0b2e.
* [Common baseline and optimized real product diagnostic](research_unturned_endpoint_complex_baseline_and_window.md),
  SHA256 9d233d9bb11c2842e62d5523f97e9621a3bd22532e3b527ceaab8125782c1cc1.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Frozen notes and public manuscripts are unchanged.
