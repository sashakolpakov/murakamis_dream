# Decay of the actual omitted endpoint rows

Private written proof, 16 November 2026.

The omitted high Newton band has an additional physical-row penalty,
beyond its previously proved polynomial norm. This estimate applies
before any remaining coupled trace is bounded. It concentrates the
uncontrolled weights near the angular endpoint on the square-root
level scale. A final proposition explains why the local low/high
cancellation exponent cannot generally be improved to half the
imaginary height for the same truncated kernel.

## 1. Original tail weights and their exact lowering products

Put
\[
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad k_0=N-m,\quad
 \theta=\pi/N,\quad\eta=(-1)^D,\quad
 c_a=2\cos((2a+1)\theta),\quad \tau_a=(D-2a)\theta.
 \tag{1}
\]
Use the original Newton polynomials
\(e_j(Z)=S_j^{-2}\prod_{h<j}(c_h-Z)\), with
\(s_j=2\sin(j\theta)\), \(S_j=\prod_{h=1}^j s_h\), the kernel
\(K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z)\), and full closing
\[
 \phi_N(h)=\eta\sum_{a<m}
       \{(4-c_a^2)h'(c_a)-c_ah(c_a)\}
                +\mathbf1_{N\ {\rm odd}}h(-2).
 \tag{2}
\]
Let \(w_N(\alpha)=2\cosh(\alpha/N)\). For \(0\le L\le m-1\), set
\[
 P_{N,L}(\alpha,Z)=\sum_{j=0}^{k_0+L}e_j(w_N(\alpha))e_j(Z),
 \qquad O_{N,L}=K_N(w_N(\alpha),Z)-P_{N,L}(\alpha,Z).
 \tag{3}
\]
Thus \(O_{N,L}\) is the omitted high band, not a value-only
replacement of the kernel. With \(r_*=m-L-2\), its exact contraction is
\[
 \phi_N(O_{N,L}f)=\sum_{a=0}^{r_*}\omega_{a,N,L}(\alpha)f(c_a),
 \qquad
 \omega_{a,N,L}=\sum_{r=a}^{r_*}e_{D-r}(w_N(\alpha))b_{ra},
 \tag{4}
\]
\[
 b_{ra}=(-1)^{r+a}
       \frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}},
 \quad s_j=2\sin(j\theta),\quad S_j=\prod_{h=1}^j s_h.
\]
An empty sum is zero. The surviving rows have
\[
 \tau_a\ge
 \begin{cases}
 (2L+3)\theta,&N\ {\rm even},\\
 (2L+4)\theta,&N\ {\rm odd}.
 \end{cases}
 \tag{5}
\]
The radical value is zero at every physical node. Consequently
the original normal in (2) differentiates \(O_{N,L}\), and no
spectator normal remains in (4). The odd simple-node contribution
is zero.

For \(p_a=m-1-a\), introduce
\[
 (A_j,B_j)=
 \begin{cases}
 ((j+\tfrac12)\theta,(j+1)\theta),&N=2m,\\
 ((j+1)\theta,(j+\tfrac32)\theta),&N=2m+1,
 \end{cases}
\]
\[
 \rho_{j,N}(\alpha,t)=
 \frac{[\cos^2A_j+\sinh^2(\alpha/(2N))]
       [\sin^2(t/2)-\sin^2A_j]}{\cos^4B_j},
 \tag{6}
\]
\[
 T_{0,N}(\alpha,t)=
 \begin{cases}
 \displaystyle \frac{\cosh(\alpha/2)}N\sin t,&N=2m,\\[3pt]
 \displaystyle
 \frac{\cosh(\alpha/2)\cosh(\alpha/(2N))}
      {N\cos^4(\theta/2)}\sin t\sin(t/2),&N=2m+1.
 \end{cases}
 \tag{7}
\]
The exact lowering identities in the pinned sources give
\[
 \boxed{\quad
 \omega_{a,N,L}(\alpha)=
 \eta(-1)^a T_{0,N}(\alpha,\tau_a)
       \sum_{l=L+1}^{p_a}\prod_{j=0}^{l-1}
                                \rho_{j,N}(\alpha,\tau_a).
 \quad}
 \tag{8}
\]
Indeed \(r=m-1-l\), and for real \(\alpha\) the sign of
\(e_{D-r}(w)b_{ra}\) is the common factor \(\eta(-1)^a\).
The exact signed identity extends to complex \(\alpha\)
because all its expressions are entire in that parameter.
The last actual term is \(l=p_a\). The next ratio has
\(\sin^2(\tau_a/2)=\sin^2 A_{p_a}\), so the chain terminates
exactly. No ratio with a vanishing denominator is used.

## 2. A uniform physical-row penalty

**Theorem 1.** For every fixed \(A<\pi\), there is \(C_A\) such that,
at both parities, for \(|\alpha|\le A\), every \(0\le L\le m-1\),
and every row in (4),
\[
 |\omega_{a,N,L}(\alpha)|
 \le C_A\min\left\{N^{3/2},
           N^4\bigl[\sin^2(\tau_a/2)\bigr]^{L+1}\right\}.
 \tag{9}
\]
The second bound in fact holds on every bounded complex
\(\alpha\)-set, without \(A<\pi\). The stricter parameter condition
will be used for shared full-kernel values in Section 3.

*Proof.* Fix a physical row and write \(z=\sin^2(\tau_a/2)\).
For \(j<l\le p_a\), all factors are before physical termination,
and
\[
 0\le z-\sin^2A_j\le z\cos^2A_j,\qquad
 |\sinh^2(\alpha/(2N))|\le C_A/N^2.
\]
Therefore
\[
 \left|\prod_{j<l}\rho_{j,N}\right|
 \le z^l
   \left(\prod_{j<l}\frac{\cos A_j}{\cos B_j}\right)^4
   \prod_{j<l}\left(1+\frac{C_A}{N^2\cos^2A_j}\right).
 \tag{10}
\]
All cosines in this inequality are positive. Since
\(B_j=A_j+\theta/2\) and \(A_{j+1}=A_j+\theta\), the intervals
\([A_j,B_j]\) are disjoint and contained in \([0,B_{l-1}]\).
Integrating \(\tan u\ge0\) gives
\[
 \prod_{j<l}\frac{\cos A_j}{\cos B_j}
 \le\frac1{\cos B_{l-1}}\le\frac1{\sin\theta}\le\frac N2.
 \tag{11}
\]
For the middle inequality, \(l\le p_a\le m-1\) gives
\(B_{l-1}\le\pi/2-\theta\) at both parities.
The case \(l=0\) is the empty product and needs no such estimate.

Likewise \(A_j\le\pi/2-3\theta/2\), and the distances
\(\pi/2-A_j\), read backwards, increase in steps of \(\theta\).
Using \(\sin u\ge2u/\pi\) for \(0\le u\le\pi/2\),
\[
 \sum_{j<l}\sec^2A_j
 \le\frac{N^2}{4}\sum_{q=0}^{\infty}(q+\tfrac32)^{-2}
 \le C N^2.
 \tag{12}
\]
Thus the last product in (10) is at most a constant depending
only on the bounded parameter set. Equations (10)--(12) imply
\[
 \left|\prod_{j<l}\rho_{j,N}\right|\le C_A N^4 z^l.
 \tag{13}
\]
The base (7) is \(O_A(N^{-1})\) uniformly over the physical grid.
There are at most \(N\) terms in (8), and \(0\le z\le1\).
Summing (13) for \(l\ge L+1\) proves the second bound in (9).
The finitely many small levels can be absorbed in the constant;
at \(N=2\) the omitted band is empty. The first bound in (9)
is the full-radical Fourier bound already proved in the
central-band source, whose parameters may be any bounded complex
set. Both estimates concern the same coefficient, so their
minimum is valid. \(\square\)

For \(L=\lfloor\delta N\rfloor\), \(0<\delta<1/2\), the pointwise
exponential penalty in (9), after polynomial factors, is
\[
             -\delta\log\bigl(\sin^2(\tau/2)\bigr).
 \tag{14}
\]
It is strictly positive on every fixed physical angular compact
away from \(\pi\). Its loss at \(\tau=\pi\) has an explicit scale.
Since
\[
 \sin^2(\tau_a/2)=\cos^2\!\left(\frac{\pi(a+1/2)}N\right),
 \qquad \log\cos x\le-x^2/2\quad(0\le x<\pi/2),
\]
one obtains
\[
 |\omega_{a,N,L}(\alpha)|
 \le C_A N^4
          \exp\left[-\frac{\delta\pi^2(a+1/2)^2}{N}\right].
 \tag{15}
\]
This describes the weights on the \(\sqrt N\) endpoint scale.
It is not a bound on a whole row after multiplying by its
remaining coupled source.

## 3. Shared coupons and all surviving traces

At one traced vertex take a fixed number \(r\) of endpoint coupons,
\[
 B_i(Z)=K_N(w_N(\alpha_i),Z),\quad
 P_i(Z)=P_{N,L}(\alpha_i,Z),\quad O_i=B_i-P_i,
 \qquad |\alpha_i|\le A<\pi.
 \tag{16}
\]
The root-disk bound in the cancellation source gives
\(|B_i(c_a)|\le1\) at every distinct physical node for all
sufficiently large \(N\), uniformly in the indicated complex disk.
The product of two \(O_i\)'s has zero values and first normals.
Thus the exact full-normal product rule is
\[
 \phi_N\!\left[\left(\prod_{i=1}^r B_i-\prod_{i=1}^r P_i\right)f\right]
   =\sum_{a\le r_*}\Omega_a f(c_a),\qquad
 \Omega_a=\sum_{i=1}^r\omega_{a,N,L}(\alpha_i)
                         \prod_{j\ne i}B_j(c_a).
 \tag{17}
\]
No \(B_j'\) or \(f'\) term is missing: in every surviving
product-rule term the single normal has already fallen on
the zero-valued factor \(O_i\). The odd simple value is zero.
Consequently
\[
 |\Omega_a|\le C_A r
      \min\left\{N^{3/2},N^4[\sin^2(\tau_a/2)]^{L+1}\right\}.
 \tag{18}
\]

Here is a coefficientwise form for the original coupled graph.
Let \(S\) be its traced vertices and \(T\subseteq S\) the vertices
with such shared endpoint products. Retain every original edge,
any joint polynomial spectator, and all original crossing and
charge coupons. Let \(Z_B\) be the resulting full trace and
\(Z_P\) the trace with every indicated product \(\prod_iB_i\)
replaced by \(\prod_iP_i\).
For \(\varnothing\ne U\subseteq T\), define
\(\mathscr Z_U(\mathbf a)\) by setting \(z_v=c_{a_v}\) at
\(v\in U\), retaining all original kernel and spectator factors
at these shared colors, using the partial endpoint products at
\(T\setminus U\), and taking the full original traces at
\(S\setminus U\). Omit the designated endpoint products at \(U\):
their contribution is already in \(\Omega_{v,a_v}\).
Keep any original charge coupon at an evaluated
vertex in \(\mathscr Z_U\); keep its crossing value explicitly below.
Expansion of (17) at distinct vertices gives
\[
 Z_B-Z_P=
 \sum_{\varnothing\ne U\subseteq T}\ 
 \sum_{0\le a_v\le r_*}
    \left[\prod_{v\in U}\Omega_{v,a_v}R_{n_v}(c_{a_v})\right]
                              \mathscr Z_U(\mathbf a).
 \tag{19}
\]
This is an identity for the original source. In particular an edge
joining two evaluated vertices remains
\(K_N(c_{a_v},c_{a_w})\); an edge to a surviving vertex remains
its original physical-boundary kernel. The remaining traces
retain all normals, carriers and their coherent sums.

For real powers \(n_v\), the crossing values have modulus one.
Writing
\[
 W_{N,L}(\tau)=
       \min\{N^{3/2},N^4[\sin^2(\tau/2)]^{L+1}\},
\]
(18)--(19) give the actual weighted bound
\[
 |Z_B-Z_P|
 \le\sum_{\varnothing\ne U\subseteq T}
       \prod_{v\in U}(C_A r_v)
       \sum_{\mathbf a}
          \left[\prod_{v\in U}W_{N,L}(\tau_{a_v})\right]
                                      |\mathscr Z_U(\mathbf a)|.
 \tag{20}
\]
Fixed derivatives in free spectator variables independent of the
designated \(\alpha_i\)'s satisfy the same formula with those
derivatives applied to \(\mathscr Z_U\).
No bound for \(\mathscr Z_U\) at the filled geometric action is
assumed or proved. The new penalty is retained before that
separate source-estimation problem.

## 4. A sharp restriction on the partial-kernel cancellation rate

The exact forcing of the adopted low/high cancellation equation
also gives a limit on a proposed stronger bound. This concerns the
same partial kernel (3), not a synthetic solution of its equation.

Fix \(\delta\in(0,1/2)\), set \(a_\delta=\sin^2(\pi\delta)\), and
suppose \(H>0\) satisfies
\[
 b:=\sinh^2(H/2),\qquad b+2a_\delta<1.
 \tag{21}
\]
This is exactly the condition that \(-iH\) belong to the
general-domain contraction set. At \(\alpha=0\), let
\[
 E_N(t)=\frac{P_{N,\lfloor\delta N\rfloor}(0,-2\cos t)}
                    {Q_N(-2\cos t)},
\]
where \(Q_N\) is the monic distinct-node polynomial, and put
\[
 I_\delta(H)=
 -\int_0^\delta
        \log\frac{b+\sin^2(\pi x)}{\cos^2(\pi x)}\,dx>0.
 \tag{22}
\]

**Proposition 2.** There is a constant \(c>0\) such that, for
all sufficiently large \(N\) at either parity,
\[
 \max_{j=-1,0,1}|E_N(-iH+2j\pi/N)|
             \ge cN^{-2}e^{-NI_\delta(H)}.
 \tag{23}
\]
If also \(H\ge\log3\), then
\[
                  I_\delta(H)\le\delta H<H/2.
 \tag{24}
\]
Consequently no neighborhood-uniform estimate
\(|E_N(t)|\le C N^C e^{-N|\Im t|/2}\) can hold near this point.
The proposition does not give that lower bound at the center
\(-iH\) alone.

*Proof.* The exact gauged equation in the cancellation source is
\[
 M_NE_N+\widetilde A_N(E_N(t-2\theta)-E_N(t))
        +\widetilde C_N(E_N(t+2\theta)-E_N(t))=\mathcal F_N,
\]
\[
 \mathcal F_N=(c_{k_*}-2)\beta_N(0)
                     \prod_{l=0}^{L-1}\rho_{l,N}(0,t),
 \quad L=\lfloor\delta N\rfloor,\quad k_*=k_0+L.
 \tag{25}
\]
The three left-hand coefficients are uniformly bounded near
\(-iH\): the source proves
\(M_N\to4\cot^2(t/2)\) and
\(\widetilde A_N,\widetilde C_N\to\cot^2(t/2)\) there.
At this point every ratio in the product is negative,
and its absolute value is
\[
 \frac{\cos^2A_l\,[b+\sin^2A_l]}{\cos^4B_l}.
 \tag{26}
\]
All factors are bounded away from zero and infinity over the
fixed interval \(0\le l/N\le\delta\). Their logarithms differ
uniformly by \(O(N^{-1})\) from
\(\log[(b+\sin^2(\pi l/N))/\cos^2(\pi l/N)]\).
A Riemann-sum estimate therefore gives
\[
 \sum_{l<L}\log|\rho_{l,N}(0,-iH)|
                         =-NI_\delta(H)+O(1).
 \tag{27}
\]
Moreover \(\beta_N(0)\) is bounded above and below by positive
constants times \(N^{-2}\), and
\(c_{k_*}-2\longrightarrow-2(1+\cos(2\pi\delta))\ne0\).
Thus \(|\mathcal F_N|\ge c_1N^{-2}e^{-NI_\delta(H)}\).
Taking absolute values in (25) proves (23).

Finally \(b\ge e^{-H}\) is equivalent to \(H\ge\log3\):
\[
 b-e^{-H}=\frac{(e^H-3)(e^H+1)}{4e^H}.
 \]
The ratio inside the logarithm in (22) is at least \(b\),
so \(-\log[(b+\sin^2(\pi x))/\cos^2(\pi x)]\le H\).
This proves (24). All three points in (23) have imaginary
height \(-H\) and approach the same center. The asserted
uniform half-height estimate would contradict (23)--(24).
\(\square\)

The forcing obstruction does not contradict the positive, generally
smaller exponential constant in the adopted cancellation theorem.
Nor does it make the restored full kernel homogeneous: the original
full kernel has its own nonzero highest-index forcing. Equations
(19)--(20) and the retained vertical currents remain part of any
comparison with the filled action. No whole-source upper bound or
geometric coefficient follows from this note.

## 5. Direct sources

The three complete direct sources were read at the following
versions, their directly used identities checked, and hashes verified.

* [Exact central band and original omitted weights](research_endpoint_central_band_half_charge_source.md),
  SHA256 a10186ce0d172eba2021d145b3eb5ced5c68f595397f47f3abac53429c6587da:
  full closing, radical weights and support, polynomial bound,
  original crossing values and coefficientwise graph placement.
* [General endpoint amplitude domain](research_endpoint_radical_general_domain.md),
  SHA256 600ae0d78f29946272ed54b600cb1f5fdf170965985a08d6e3d9201303722074:
  exact bases, both-parity lowering products and physical termination.
* [Actual low/high exponential cancellation](research_endpoint_low_high_exponential_cancellation.md),
  SHA256 594bd802439d08e3dfe32f6cfa1027d291b36c502061dc7723fd0a8734527f5d:
  root-disk bound, shared-coupon full-normal identity, exact
  gauged forcing equation and the distinction from the full kernel.

Only written mathematics, text reads and hashes were used. No
mathematical program, numerical experiment, test or compilation was
run. Adopted notes and public manuscripts are unchanged.
