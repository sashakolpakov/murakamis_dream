# Two half-plane representatives and the exact endpoint-product interface

Private written proof, 16 November 2026.

Every fixed product of full microscopic endpoint kernels, at an
original traced vertex, has an exact pair of representatives with
polynomial bounds on their respective half-planes. Each preserves
all angular Hermite jets. Using the lower representative below the
real axis and the upper representative above it leaves an explicit
holomorphic interface current. The original Gaussian, all spectators,
and every vertical side remain.

The projection and Fourier folding are archived identities. The new
assembly applies them to the actual full shared endpoint product,
with a polynomial coefficient bound and the complete relative
contour. No intermediate Newton cutoff is introduced.

## 1. Full endpoint products and a polynomial coefficient bound

Use
\[
 N\ge2,\quad D=N-1,\quad\eta=(-1)^D,\quad
 c_a=2\cos((2a+1)\pi/N),\quad P_N(Z)=2T_N(Z/2)+2,
\]
\[
 e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z),\quad
 S_j=\prod_{a=1}^j2\sin(\pi a/N),\quad S_0=1,\quad
 K_N(w,Z)=\sum_{j=0}^D e_j(w)e_j(Z).
 \tag{1}
\]
Fix \(r\ge0\) and \(A<\infty\), independent of the level. For
complex parameters \(|\alpha_i|\le A\), set
\[
 w_i=2\cosh(\alpha_i/N),\quad
 Q_N(Z)=\prod_{i=1}^rK_N(w_i,Z),\quad
 C_N(Z)=\operatorname{rem}_{P_N}Q_N(Z).
 \tag{2}
\]
The empty product is one. Reduction in (2) occurs only in an
originally traced variable, after its endpoint kernels have been
multiplied. It preserves every double-root value and first normal,
and the odd simple-root value. All other factors remain untouched.

There are constants \(C,p\), depending only on \(A,r\), such that
\[
 \sup_{Z\in[-2,2]}|Q_N(Z)|+\|\widehat C_N\|_1\le CN^p,\qquad
 C_N(-2\cos t)=\beta_0+
                \sum_{k=1}^D\beta_k(e^{-ikt}+e^{ikt}),
 \tag{3}
\]
where \(\|\widehat C_N\|_1=|\beta_0|+2\sum_{k=1}^D|\beta_k|\).

To prove this for arbitrary bounded microscopic parameters, choose a
fixed integer \(b\ge0\) with \((2b+1)\pi>A\). For sufficiently large
\(N\),
\[
                         |w_i-2|\le2-c_b .
 \tag{4}
\]
The endpoint source proves the physical-row factorization
\[
 F_{j,N}(w)=K_N(c_j,w)
   =\prod_{\nu=1}^j\frac{r_{j,\nu}-w}{r_{j,\nu}-c_0},
                         \qquad r_{j,\nu}>2.
\]
Thus, for every distinct physical row,
\[
 |F_{j,N}(w_i)|\le F_{j,N}(c_b)
       =F_{b,N}(c_j)\le F_{b,N}(-2)\le C_bN^{2b}.
 \tag{5}
\]
The last inequality follows directly from its exact positive formula
\[
 F_{b,N}(-2)=\sum_{k=0}^b
     \frac{S_{b+k}}{S_{b-k}S_k^4}\prod_{h<k}(c_h+2).
 \tag{6}
\]
For fixed \(b,k\), the factorial quotient is \(O_b(N^{2k})\);
the remaining factors are at most four. The preceding inequality
in (5) also follows from the root product.

The low kernel is the ordinary degree-\(J\) interpolant of these
values, where \(J=\lfloor(N-1)/2\rfloor\). Its real-interval norm
is at most \(N\max_j|F_{j,N}(w_i)|\), by the endpoint source's
exact cosine interpolation bound. The remaining radical polynomials
satisfy
\[
 |e_{D-a}(-2\cos t)|\le\sqrt{N-1}\,e^{D|\Im t|}
                    \quad(0\le a<\lfloor N/2\rfloor).
 \tag{7}
\]
Use \(t=\pi-i\alpha_i/N\) in their first color and a real angle in
the second. The at most \(N/2\) terms cost at most \(N^2e^A\).
Hence each full kernel, and then \(Q_N\), has polynomial real norm.
The finitely many smaller levels, including \(N=2\), are absorbed
in the constant.

The Laurent degree of \(Q_N(-2\cos t)\) is at most \(rD\).
Its Fourier coefficient sum is therefore at most \(2rD+1\) times
its real-period norm. Exact full-Hermite Fourier folding gives
\[
 \widehat C_N(m)=\sum_{\ell\in\mathbb Z}
       (\ell+1)\eta^\ell\widehat Q_N(m+\ell N),
                         \qquad 1\le m<N,
 \tag{8}
\]
together with its even zero-frequency formula. Only \(O_r(1)\)
alias blocks occur; all their weights are \(O_r(1)\).
Consequently folding increases the coefficient norm by at most
a constant depending on \(r\), proving (3).
All identities are holomorphic in the parameters. Fixed parameter
derivatives retain polynomial bounds on smaller sets by Cauchy's
formula on a larger bounded parameter set.

## 2. Two exact representatives with their full normals

Put \(z=e^{-it}\), and abbreviate \(C(t)=C_N(-2\cos t)\). Define
\[
 \begin{split}
 C_-(t)&=\beta_0+\sum_{k=1}^D\beta_k
              \{z^k+2\eta z^{N-k}-z^{2N-k}\},\\
 C_+(t)&=C_-(-t),\\
 A_-(t)&=\sum_{k=1}^D\beta_k z^{N-k},\qquad A_+(t)=A_-(-t).
 \end{split}
 \tag{9}
\]
The archived one-sided identity is
\[
 z^{-k}\equiv2\eta z^{N-k}-z^{2N-k}
                              \pmod{(z^N-\eta)^2}.
 \tag{10}
\]
It proves that each \(C_\pm\) separately has all angular values
and first derivatives of \(C\) on the physical grid
\[
              \tau_j=\pi(D-2j)/N,\qquad z_j^N=\eta .
 \tag{11}
\]
At double spectral roots these are the original spectral jets.
At the odd simple root \(t=0\), (10) preserves the value and the
zero angular derivative of the original even function. No extra
spectral normal is imposed there. The representatives need not be
even off the grid; no ordinary spectral descent is claimed for them.
The algebraic proof of (10) works also at \(N=2\).

Every exponent in \(C_-,A_-\) is nonnegative. Equation (3) therefore
gives
\[
 \sup_{\Im t\le0}(|C_-|+|A_-|)
  +\sup_{\Im t\ge0}(|C_+|+|A_+|)\le C'N^{p'}.
 \tag{12}
\]
Each fixed angular derivative adds only a power of \(N\).
For the original double-pole grid kernel
\[
                         W_N(t)=\frac{z^N}{(1-\eta z^N)^2},
 \tag{13}
\]
direct subtraction gives the exact identities
\[
 \boxed{\qquad
 CW_N=C_-W_N+A_-=C_+W_N+A_+.
 \qquad}
 \tag{14}
\]
In particular the correction after multiplication by the grid
kernel is holomorphic, with no remaining grid pole.

## 3. The original contour and its oriented interface

Let \(\Gamma_H\), \(H>0\), be the counterclockwise rectangle with
corners \(\pm\pi\pm iH\). Its lower exterior half \(E_-\) runs
from \(-\pi\) down the left side, across the bottom from left to
right, and up the right side to \(\pi\). Its upper exterior half
\(E_+\) runs from \(\pi\) up the right side, across the top from
right to left, and down to \(-\pi\). Thus every vertical half-side
is included.

Let \(F(t;\mathbf u)\) be the actual remaining even spectator,
holomorphic on a neighborhood of this closed rectangle. It may
retain every other trace variable, edge kernel, coupon, and
ordinary free boundary parameter jointly. For the original integer
crossing power \(n\), set
\[
 g(t)=\sin t\,e^{inNt^2/(4\pi)}F(t;\mathbf u),\qquad
 \mathfrak c_{N,n}=\exp\{\pi i nD^2/(4N)\}.
 \tag{15}
\]
The original full derivative-residue formula is
\[
 \phi_N(R^nQ_NF)=
 -\frac{N^2\mathfrak c_{N,n}}{2\pi i}
                       \oint_{\Gamma_H}CW_Ng\,dt .
 \tag{16}
\]
Here \(F\) on the left means the original spectral spectator or
its trace-compatible analytic angular representative. Reduction
(2) preserves the full jets before the residue formula is applied.
For the normalization, at each \(\tau_j\) the kernel has expansion
\(W_N(t)=-\eta/[N^2(t-\tau_j)^2]+O(1)\), with no simple-pole
term. Thus (16) is exactly the original derivative sum
\(\eta\mathfrak c_{N,n}\sum_j(Cg)'(\tau_j)\).
At the odd zero angle the derivative of \(\sin t\) supplies the
simple spectral value; this check also covers \(N=2\).

**Theorem.** With these conventions,
\[
 \boxed{\begin{split}
 \oint_{\Gamma_H}CW_Ng\,dt
 ={}&\int_{E_-}C_-W_Ng\,dt+\int_{E_+}C_+W_Ng\,dt\\
    &+\int_{-\pi}^{\pi}(A_--A_+)g\,dt .
 \end{split}}
 \tag{17}
\]
The exterior amplitudes obey (12); the interface amplitude is
polynomially bounded on its real path. Every original normal,
Gaussian factor, spectator, and vertical side remains.

*Proof.* Apply the first expression in (14) on \(E_-\) and the
second on \(E_+\). Holomorphy gives
\[
 \int_{E_-}A_-g\,dt=\int_{-\pi}^{\pi}A_-g\,dt,\qquad
 \int_{E_+}A_+g\,dt=-\int_{-\pi}^{\pi}A_+g\,dt.
 \tag{18}
\]
Indeed the lower half-rectangle's positive real boundary runs
from \(\pi\) to \(-\pi\); the upper one's runs oppositely.
Adding proves (17). The corrections have no grid poles, so zero
at odd levels causes no exception. \(\square\)

The interface is explicitly a finite sum of continuous Fourier
integrals:
\[
 \begin{split}
 \int_{-\pi}^{\pi}(A_--A_+)g\,dt
 =-i\sum_{k=1}^D\beta_k\int_{-\pi}^{\pi}
 &\{\cos((N-k-1)t)-\cos((N-k+1)t)\}\\
 &\times e^{inNt^2/(4\pi)}F(t;\mathbf u)\,dt .
 \end{split}
 \tag{19}
\]
These are ordinary integrals, not substituted finite charged traces.
Their frequencies include zero at \(k=D\); no separate exponential
smallness is asserted. Both \(A_--A_+\) and \(g\) are odd, so their
product is even and generally does not integrate to zero.
Moving this interface back to the exterior halves restores (14);
it does not cancel an endpoint current for free.

## 4. Shared graph placement and scope

All identities are coefficientwise in uncontracted variables.
At every traced vertex multiply its full endpoint coupons first,
take the full-Hermite remainder, and then apply (9)--(17).
Operations in distinct variables commute. Their tensor product
gives the finite sum of exterior-half and interface integrals for
a fixed graph, retaining every shared edge and all remaining
original traces. Outside mixed derivatives commute with the
identities. The spectator itself is not replaced by a value-only
interpolant.

There is no canonical reduction in an ordinary free variable.
If the unreduced product \(Q_N\) is retained on separate contour
sides, its difference from \(C_N\) has an additional holomorphic
current after multiplication by \(W_N\); that current must remain.
In (16), full quotient reduction has already been performed inside
the exact closed original trace.

The construction uses only full endpoint products. It is independent
of a low/high truncation or a central physical window. It avoids a
globally even moderate representative by using two angular
representatives with the explicit interface. It supplies no bound
for their Gaussian-spectator product at the filled action and no
general inserted-descendant estimate.

## 5. Coverage and direct sources

Projection (10), the full derivative-residue normalization, and
Fourier folding are existing results. The additional assembly is
their cutoff-independent use for all fixed shared microscopic
endpoint products, with the polynomial bound and the fully oriented
relative interface (17).

The following complete sources were read at unchanged versions;
their directly used implications and final hashes were checked:

* [One-sided Hermite projection](research_one_sided_hermite_projection.md),
  SHA256 efa82935ada9aa9e06dcbd5d20d5e05357859986896b0b73a93eb78a4bb81cf4:
  exact angular projection, full derivative-residue trace, and
  transferred contour terms.
* [Boundary crossing packet preservation](research_boundary_crossing_packet_preservation.md),
  SHA256 a2f9cadf0fd6f23889ea7d20b469055fe33cb9df4d971668a2923666983cfec8:
  full-Hermite Fourier folding with all aliases and odd ramification.
* [Full-period endpoint kernel reduction](research_full_period_endpoint_kernel_reduction.md),
  SHA256 a1d67ac803c0160bbfdacaa96a6fde9dc1ffae06fc39eb94f0416dcf2ecef76e:
  actual row root product and formula, ordinary interpolation bound,
  and endpoint/full-normal conventions.
* [High Newton radical contraction](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  exact both-parity split and the radical Fourier bound (7).

Only written mathematics, source-text reads, and hashes were used.
No mathematical program, numerical experiment, test, or compilation
was run. Adopted notes and public manuscripts were unchanged.

