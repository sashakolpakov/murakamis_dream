# The vertical current after the full radical is contracted

Private written proof, 16 November 2026.

Exact high-Newton contraction leaves a kernel of approximately half
the original degree. Its growth at two positive endpoint heights is
smaller, but is still exponential. The actual all-removed vertical
integral of this remaining kernel has a nonzero asymptotic under the
degree and power condition below. Thus radical contraction alone
does not give a zero-cost transfer of the saturated angle envelope.
The full horizontal and vertical sum remains a separate object.

## 1. The remaining ordinary kernel

Retain the original normalization
\[
 \begin{gathered}
 N\ge2,\quad D=N-1,\quad \eta=(-1)^D,\quad
 m=\lfloor N/2\rfloor,\quad L=D-m,\\
 c_j=2\cos((2j+1)\pi/N),\quad
 s_j=2\sin(\pi j/N),\quad S_k=\prod_{j=1}^k s_j,\quad S_0=1,\\
 e_k(C)=S_k^{-2}\prod_{j<k}(c_j-C),\quad
 P_N(C)=2T_N(C/2)+2,\quad
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f .
 \end{gathered}                                                    \tag{1}
\]
The exact split is
\[
 K_N(C,C')=K_N^{\rm low}(C,C')+
             \sum_{r=0}^{m-1}e_{D-r}(C)e_{D-r}(C'),\qquad
 K_N^{\rm low}(C,C')=\sum_{k=0}^{L}e_k(C)e_k(C').
 \tag{2}
\]
At odd levels the middle polynomial \(e_m\) belongs to the low
kernel. At even levels the low kernel ends at \(e_{m-1}\).
The radical contraction source gives an exact matching expansion
for the difference of the corresponding original graph traces.
Every radical insertion consumes its actual first-normal term.
The low kernel in (2) is an ordinary polynomial with its own
ordinary derivatives; it is not asserted to share the full kernel's
first normals by itself.

For \(h\ge0\) write \(w_h=2\cosh h\), and for \(h>0\) put
\[
 r(h)=\operatorname{sech}^2(h/2),\qquad
 a_{\rm ev}(h)=\frac{r(h)}2,\qquad
 a_{\rm odd}(h)=\frac{\sqrt{r(h)}}2=\frac1{2\cosh(h/2)} .
 \tag{3}
\]
The last expression specifies the holomorphic branch near a positive
real height. Let \(\epsilon\) denote the parity of \(N\), and define
\[
 \mathcal K_\epsilon(h,h')=
 \frac{a_\epsilon(h)a_\epsilon(h')}
      {1-r(h)r(h')}.
 \tag{4}
\]
This is positive for real \(h,h'>0\).

**Lemma 1.** Uniformly on compact positive height sets,
\[
 K_N^{\rm low}(w_h,w_{h'})
 =N^{-2}e^{N(h+h')/2}
       \left\{\mathcal K_\epsilon(h,h')+O_{\rm hol}(N^{-2})\right\}.
 \tag{5}
\]
The error is holomorphic on a fixed complex neighborhood of each
such compact and obeys the same bound after fixed derivatives.
On the whole nonnegative height quadrant one also has
\[
 0<K_N^{\rm low}(w_h,w_{h'})
       \le (L+1)e^{N(h+h')/2}.
 \tag{6}
\]

*Proof.* The exact final Newton polynomial is
\[
 e_L(w_h)=(-1)^L
 \begin{cases}
 \displaystyle\frac{4\cosh(Nh/2)}
        {N(2\cosh h+2\cos(\pi/N))},&N\ {\rm even},\\[2mm]
 \displaystyle\frac{\cosh(Nh/2)}{N\cosh(h/2)},&N\ {\rm odd}.
 \end{cases}                                                     \tag{7}
\]
For even \(N=2m\), the monic polynomial of all distinct double
nodes is \(2T_m(C/2)\), and \(S_m^2=2N\). This first gives
\(e_m(w_h)=(-1)^m\cosh(Nh/2)/N\). Removing its last factor,
whose node is \(c_{m-1}=-2\cos(\pi/N)\), gives the first line.
For odd \(N=2m+1\), the monic polynomial of the double nodes is
\(U_m(C/2)-U_{m-1}(C/2)\), while \(S_m^2=N\).
At \(C=2\cosh h\) that polynomial is
\(\cosh(Nh/2)/\cosh(h/2)\), giving the second line.
The sine-product normalizations follow by pairing the factors in
\(S_D=N\). These derivations also verify the small levels directly.

The squared-sine ratios
\[
 \frac{|e_{k+1}(2)|}{|e_k(2)|}
   =\frac{\sin^2((k+\tfrac12)\pi/N)}
          {\sin^2((k+1)\pi/N)}
 \tag{8}
\]
make the sequence decrease and then increase. Its two end values
are \(1\) and \([N^2\sin^2(\pi/(2N))]^{-1}\le1\).
Thus \(|e_k(2)|\le1\) for every \(k\).
For \(k\le L\), extend the partial positive product
\(\prod_{j<k}(w-c_j)/(2-c_j)\), with \(w\ge2\), over all
distinct double nodes. The resulting product is
\[
 \begin{cases}
 \cosh(Nh/2),&N\ {\rm even},\\
 \cosh(Nh/2)/\cosh(h/2),&N\ {\rm odd},
 \end{cases}
 \qquad w=w_h .
 \tag{9}
\]
Both are at most \(e^{Nh/2}\). Each \(e_k(w)\) has sign
\((-1)^k\), so summing the positive same-index products proves (6).
This argument includes \(h=0\).

For (5), choose a fixed complex neighborhood of the positive compact
with \(\Re w_h,\Re w_{h'}\ge2+\delta\). Set
\[
 b_{N,j}(h)=
       \frac{s_{L-j}^2}{w_h-c_{L-j-1}},\qquad 0\le j<L .
 \tag{10}
\]
These are the negatives of the single-polynomial backward ratios.
For sufficiently large \(N\), the difference-of-cosines estimate
\[
 \Re w-c_k-s_{k+1}^2\ge\delta-2\pi/N\ge\delta/2
 \tag{11}
\]
gives \(|b_{N,j}(h)|\le\vartheta<1\), uniformly over the entire
index range. After reducing the complex neighborhood if necessary,
\(|r(h)|\le\vartheta<1\) as well.
Since \(L=N/2+O(1)\), the elementary sine and cosine estimates at
the middle index give
\[
 |b_{N,j}(h)-r(h)|
               \le C(j+1)^2N^{-2}\qquad(0\le j<L).
 \tag{12}
\]
The denominators in (10) are bounded below by \(\delta\).
The numerator differs from \(4\), and the node differs from
\(-2\), by \(O((j+1)^2/N^2)\); this proves (12), uniformly even
when its right side is of order one.

For \(\ell\) backward steps the two signs cancel, and the relative
kernel summand is
\(\prod_{j<\ell}b_{N,j}(h)b_{N,j}(h')\).
Telescoping the difference from \([r(h)r(h')]^\ell\), using
(11)--(12), bounds it by
\(C N^{-2}\ell^3\vartheta^{2\ell-2}\).
Summing this estimate and the exponentially small geometric tail
beyond \(L\) gives
\[
 \frac{K_N^{\rm low}(w_h,w_{h'})}{e_L(w_h)e_L(w_{h'})}
       =\frac1{1-r(h)r(h')}+O_{\rm hol}(N^{-2}).
 \tag{13}
\]
Formula (7) is
\[
 e_L(w_h)=(-1)^LN^{-1}e^{Nh/2}
                 \{a_\epsilon(h)+O_{\rm hol}(N^{-2})\}.
 \tag{14}
\]
The exponentially small second term of the hyperbolic cosine has
been included in the error. Equations (13)--(14) prove (5).
Cauchy estimates on smaller fixed neighborhoods prove all stated
derivative bounds. \(\square\)

## 2. The complete low-kernel vertical integral

Let \(\Gamma=(V,E)\) be a fixed nonempty finite loopless simple graph.
Every vertex is selected; there is no outside vertex or extra coupon.
Each edge is counted once. Write \(a=|V|\), \(b=|E|\), and
let \(d_v\) be the degree. Fix \(H_v>0\) and integer \(n_v\ne0\)
such that
\[
 d_v\ge1,\qquad d_v+|n_v|>2\quad(v\in V).
 \tag{15}
\]
In particular, every graph without isolated vertices with all
\(|n_v|\ge2\) satisfies (15).

Retain the original full-period unit density
\[
 \begin{gathered}
 C_{N,n}=e^{\pi i n(N-1)^2/(4N)},\qquad
 \Omega_{N,n}=C_{N,n}e^{inN\pi/4},\\
 \rho_{N,n,1}(h)=
 \frac{2i\eta N^2\Omega_{N,n}}{\pi}
 \frac{\sinh h\,e^{-inNh^2/(4\pi)}\sinh(nNh/2)}
      {P_N(w_h)} .
 \end{gathered}                                                   \tag{16}
\]
This density comes from the original value and first-normal trace;
the odd simple-node value is also included in that contour identity.
Define the all-removed term of the remaining low source by
\[
 \mathcal I_{\Gamma,N}^{\rm low}=
 \int_{\prod_v[0,H_v]}
       \prod_v\rho_{N,n_v,1}(h_v)
       \prod_{\{v,w\}\in E}K_N^{\rm low}(w_{h_v},w_{h_w})
       \prod_vdh_v .
 \tag{17}
\]
The other terms of the exact radical matching expansion are retained
separately; (17) is not substituted for the full kernel current.

Put
\[
 \lambda_v=\frac{d_v+|n_v|}{2}-1>0,\qquad
 \Phi_v(h)=\lambda_vh-\frac{in_vh^2}{4\pi}.
 \tag{18}
\]

**Theorem 2.** Along each parity, uniformly on compact positive
height sets,
\[
 \mathcal I_{\Gamma,N}^{\rm low}
 =\mathcal B_{\Gamma,N}(\mathbf H)\,
        N^{\,a-2b}e^{N\sum_v\Phi_v(H_v)}
                   (1+O(N^{-1})),
 \tag{19}
\]
where
\[
 \mathcal B_{\Gamma,N}(\mathbf H)=
 \left(\frac{i\eta}{\pi}\right)^a
 \left[\prod_v
  \frac{\operatorname{sgn}(n_v)\Omega_{N,n_v}\sinh H_v}
       {\lambda_v-in_vH_v/(2\pi)}\right]
 \prod_{\{v,w\}\in E}\mathcal K_\epsilon(H_v,H_w).
 \tag{20}
\]
Its modulus is uniformly bounded above and below by positive
constants. Both parities therefore have the same actual rate
\[
 \lim_{N\to\infty}N^{-1}\log|\mathcal I_{\Gamma,N}^{\rm low}|
       =\sum_v\left(\frac{d_v+|n_v|}{2}-1\right)H_v .
 \tag{21}
\]

*Proof.* The exact density satisfies
\[
 |\rho_{N,n,1}(h)|\le CN^2e^{N(|n|/2-1)h}
                     \quad(0\le h\le H).
 \tag{22}
\]
Combining (6) and (22) bounds the whole integrand by
\[
 CN^{2a+b}e^{N\sum_v\lambda_vh_v}.
 \tag{23}
\]
Since every \(\lambda_v>0\), the integral outside
\(\prod_v[H_v/2,H_v]\) has rate at most
\(\sum_v\lambda_vH_v-\tfrac12\min_v\lambda_vH_v\).
All axes and small-height faces are thus included with a fixed
exponential gap.

On this positive corner, (16) is exactly
\[
 \rho_{N,n,1}(h)=
 \frac{i\eta\operatorname{sgn}(n)\Omega_{N,n}}{\pi}N^2
 \sinh h\,e^{N\{(|n|/2-1)h-inh^2/(4\pi)\}}
 \frac{1-e^{-|n|Nh}}{(1+e^{-Nh})^2}.
 \tag{24}
\]
The final ratio is \(1+O_{\rm hol}(e^{-cN})\) on smaller fixed
neighborhoods of the corner. Substituting (5) into (17) leaves
\[
 \left(\frac{i\eta}{\pi}\right)^a
 \left(\prod_v\operatorname{sgn}(n_v)\Omega_{N,n_v}\right)
 N^{2a-2b}
 \int
 \{A_\epsilon(\mathbf h)+O_{\rm hol}(N^{-2})\}
                 e^{N\sum_v\Phi_v(h_v)}\,d\mathbf h ,
 \tag{25}
\]
where the integral is over the corner and
\[
 A_\epsilon(\mathbf h)=
          \prod_v\sinh h_v
          \prod_{\{v,w\}\in E}\mathcal K_\epsilon(h_v,h_w)>0 .
 \tag{26}
\]
This amplitude can couple neighboring heights. It is smooth with
uniformly bounded fixed derivatives on the chosen corner.

For completeness, multidimensional endpoint Laplace applies here
without assuming that amplitude factorizes. Set
\(x_v=N(H_v-h_v)\). Then
\[
 N[\Phi_v(H_v-x_v/N)-\Phi_v(H_v)]
  =-\Phi_v'(H_v)x_v-\frac{in_vx_v^2}{4\pi N},
 \qquad \Re\Phi_v'(H_v)=\lambda_v>0 .
 \tag{27}
\]
The change in \(A_\epsilon\) is bounded by
\(C\sum_vx_v/N\), and the change in the final quadratic exponential
from one is bounded by \(C\sum_vx_v^2/N\) on real \(x_v\).
All these errors integrate against
\(e^{-\sum_v\lambda_vx_v}\) with \(O(N^{-1})\) cost.
Extending the finite \(x_v\)-intervals to \([0,\infty)\) has
exponentially small cost. The leading integral is therefore
\[
 N^{-a}e^{N\sum_v\Phi_v(H_v)}
       A_\epsilon(\mathbf H)
       \prod_v\frac1{\Phi_v'(H_v)}(1+O(N^{-1})).
 \tag{28}
\]
The error term in (25) has absolute integral
\(O(N^{-a-2}e^{N\sum_v\lambda_vH_v})\).
Together with (23), these facts prove (19)--(20).
Positivity in (26) and the nonzero derivatives in (27) give the
uniform lower bound for the coefficient and (21). \(\square\)

## 3. Consequence for grouped-source estimates

The density-only rate for this all-removed graph is
\(\sum_v(|n_v|/2-1)H_v\). The remaining low kernel contributes
the additional rate
\[
 \frac12\sum_v d_vH_v
       =\frac12\sum_{\{v,w\}\in E}(H_v+H_w)>0 .
 \tag{29}
\]
This is an actual integrated rate, with a nonzero signed coefficient,
and not merely a pointwise bound on an off-grid polynomial.
Removing and contracting the full high radical reduces the internal
kernel cost by half in this source, but does not remove it.

Consequently, a pointwise or all-vertical bound for the remaining low
source using only the zero-cost saturated angle envelope cannot hold
in this generality. A useful estimate must pay (29), compare it with
an available action reserve, or combine it with horizontal terms
before estimating. The theorem does not rule out any of those
possibilities. It also does not assign (21) to the complete original
trace: that trace includes both the low-source horizontal currents
and the exact radical matching contributions.

The all-removed hypothesis eliminates surviving traces only in this
theorem's specified graph. It does not justify deleting such traces
or their shared boundary products in a larger source. Likewise,
the condition (15) is used for the strict endpoint maximum. Zero
powers make their actual unit currents vanish, and the excluded
degree-one, absolute-power-one case has zero \(\lambda_v\);
neither is covered by (19).

## 4. Coverage and source verification

The exact low/high split, original high-radical matching contraction,
and middle Newton polynomials are archived. The full-kernel
all-removed theorem already proves why its oscillatory endpoint
integrals can have nonzero exponential growth. The new step is the
explicit parity-dependent low-kernel coefficient (5), the uniform
half-height bound (6), and their actual integrated consequence
after the entire radical has been removed.

Both complete direct sources were read, the used implications
rechecked, and their unchanged hashes verified:

* [Full radical contraction and original low kernel](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03.
* [Actual full-kernel all-removed current and its normalization](research_all_removed_vertical_current_asymptotic.md),
  SHA256 ac051b227228ea390576cb9426ec052fe60910dde483cae0327838985b8d154f.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Frozen notes and public manuscripts are unchanged.
