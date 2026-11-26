# Bulk Fourier coefficients of one original endpoint kernel

Private written proof, 16 November 2026.

For one microscopic endpoint color, the upper half of the original
kernel's Fourier coefficients has an exact checkerboard sign and a
positive finite sum. On every fixed degree interval strictly between
zero and the fold, a short prefix of that sum is an analytic unit of
order \(N^{-1}\). Its relative error at the physical degree nodes is
exponentially small. A localized sinc correction gives one exact
analytic interpolant on a fixed complex strip, with the same leading
coefficient and no extensive phase after the checkerboard is removed.

This is a statement about the ordinary original kernel, including
its full spectral normals. It is not a bound for a whole interface
integral. The checkerboard, its complex growth, the two degree
endpoints, and all other source factors remain.

## 1. Original coefficients and the exact positive sum

Use the original normalization
\[
 \theta=\pi/N,\quad q=e^{i\theta},\quad D=N-1,\quad
 \eta=(-1)^D,\qquad s_j=2\sin(j\theta),\quad
 S_j=\prod_{r=1}^j s_r,\quad S_0=1,
\]
\[
 c_j=2\cos((2j+1)\theta),\quad
 e_j(Z)=S_j^{-2}\prod_{h<j}(c_h-Z),\quad
 K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z),
\]
\[
 P_N(Z)=2T_N(Z/2)+2=\prod_{j=0}^{D}(Z-c_j).
 \tag{1}
\]
Here \(N\ge2\). Fix real \(\alpha\), put
\[
 w=w_N(\alpha)=2\cosh(\alpha/N),
\qquad
 K_N(w,-z-z^{-1})
   =b_{0,N}+\sum_{k=1}^{D}b_{k,N}(z^k+z^{-k}).
 \tag{2}
\]
In angular notation \(z=e^{-it}\). These are ordinary Laurent
coefficients, before taking any physical quotient.

**Proposition 1.** For \(1\le s\le\lfloor N/2\rfloor\),
\[
 b_{N-s,N}=\eta(-1)^{s-1}\beta_{s,N},\qquad
 \beta_{s,N}=\sum_{m=1}^{s}T_{m,s,N}>0,
 \tag{3}
\]
where
\[
 T_{m,s,N}=
 \frac{P_N(w)S_{m-1}^{\,4}}{N^4}
 \frac{S_{s+m-1}}
 {S_{s-m}S_{2m-1}\prod_{h=0}^{m-1}(w-c_h)}.
 \tag{4}
\]
For \(1\le m<s\),
\[
 \frac{T_{m+1,s,N}}{T_{m,s,N}}
 =\frac{s_m^4s_{s+m}s_{s-m}}
 {(w-c_m)s_{2m}s_{2m+1}}.
 \tag{5}
\]
The formulas apply at both parities, including \(N=2\).

**Proof.** The elementary sine product gives \(S_{N-1}=N\), hence
\(S_{N-m}=N/S_{m-1}\). The last \(m\) roots in (1) are
\(c_0,\ldots,c_{m-1}\) in reverse order. Therefore
\[
 e_{N-m}(w)=
 (-1)^{N-m}\frac{P_N(w)S_{m-1}^2}
 {N^2\prod_{h<m}(w-c_h)}.
 \tag{6}
\]
Also
\[
 P_N(-z-z^{-1})=(-1)^Nz^{-N}(1-\eta z^N)^2.
 \tag{7}
\]
Writing
\[
 \Pi_m(z)=\prod_{h=0}^{m-1}
 (1+q^{2h+1}z)(1+q^{-(2h+1)}z),
\]
substitution in (6) gives the exact rational expression
\[
 e_{N-m}(-z-z^{-1})
 =\frac{S_{m-1}^2}{N^2}\,
       \frac{z^{m-N}(1-\eta z^N)^2}{\Pi_m(z)}.
 \tag{8}
\]
The right side is the displayed ordinary Laurent polynomial.
Equivalently, multiplying by
\(W_N(z)=z^N/(1-\eta z^N)^2\) cancels the full spectral relation.

The factors of \(\Pi_m\) are consecutive:
\[
 \Pi_m(z)=\prod_{j=0}^{2m-1}
             (1+q^{-(2m-1)+2j}z).
\]
For \(0\le\ell\le s-m\),
\[
 [z^\ell]\Pi_m(z)^{-1}
   =(-1)^\ell\frac{S_{2m+\ell-1}}{S_\ell S_{2m-1}}.
 \tag{9}
\]
For completeness, set \(Q=q^2\), \(a=q^{-(2m-1)}\), and
\(f(z)=\prod_{j=0}^{2m-1}(1+aQ^jz)^{-1}\).
The identity
\((1+aQ^{2m}z)f(Qz)=(1+az)f(z)\) gives, for its coefficients,
\[
 [z^\ell]f=-a\,\frac{1-Q^{2m+\ell-1}}{1-Q^\ell}
                       [z^{\ell-1}]f.
\]
No denominator vanishes in the range in question. Replacing
\(1-Q^r\) by \(-iq^rs_r\) cancels all powers of \(q\) and proves
(9), starting at \([z^0]f=1\).

Only Newton indices \(N-m\) with \(m\le s\) contribute to the
coefficient of \(z^{s-N}\) in (2). In (8) its coefficient comes
from \(\ell=s-m<N\), so the nonconstant terms of
\((1-\eta z^N)^2\) do not contribute. Multiply (6), (8), and (9).
The sign is
\((-1)^{N-m+s-m}=(-1)^{N+s}=\eta(-1)^{s-1}\), independent
of \(m\). This proves (3)--(4). All remaining factors are positive:
their sine indices lie between \(1\) and \(2s-1\le N-1\),
\(w-c_h>0\), and
\[
                         P_N(w)=4\cosh^2(\alpha/2)>0.
 \tag{10}
\]
Taking the quotient of consecutive terms proves (5).
\(\square\)

## 2. A uniform ratio below the fold

Fix \(b<1/2\), put \(z_b=\sin^2(\pi b)<1\) and
\(c_b=\cos(\pi b)>0\). For all sufficiently large \(N\),
uniformly in real \(\alpha\) and \(1\le m<s\le bN\),
\[
             0<\frac{T_{m+1,s,N}}{T_{m,s,N}}
                 \le q_b:=\frac{1+z_b}{2}<1.
 \tag{11}
\]
One sufficient level threshold is
\[
                   N\ge\frac{\pi z_b}{c_b(1-z_b)}.
 \tag{12}
\]
This is an eventual-level bound on a fixed bulk interval, not a
bound uniform up to the moving fold.

To prove it, put \(u=m\theta\), \(v=(m+1/2)\theta\), and
\(z_s=\sin^2(s\theta)\). Since \(w\ge2\),
\(w-c_m\ge4\sin^2v\). The sine products in (5) yield
\[
 \frac{T_{m+1,s,N}}{T_{m,s,N}}
 \le
 \left(\frac{\sin u}{\sin v}\right)^3
       \frac{z_s-\sin^2u}{\cos u\cos v}.
 \tag{13}
\]
Here \(0<u<v<s\theta\le\pi b\), and
\(z_s-\sin^2u\le z_s\cos^2u\). Consequently (13) is at most
\[
 z_s\frac{\cos u}{\cos v}
 \le z_b\left(1+\frac{\pi}{2Nc_b}\right),
 \tag{14}
\]
because \(\cos u-\cos v\le\theta/2\). Equations (11)--(12)
follow.

## 3. Analytic prefix and its nonzero leading coefficient

Fix
\[
 0<a<b<\tfrac12,\qquad |\alpha|\le A,\quad \alpha\in\mathbb R,
 \qquad A<\infty.
 \tag{15}
\]
Choose \(0<a_0<a<b<b_0<1/2\), and
\[
 0<\sigma<\min\{a_0,\tfrac12-b_0\},\qquad
 M_N=\lfloor\sigma N\rfloor.
 \tag{16}
\]
All following assertions are for sufficiently large \(N\), in
particular \(M_N\ge1\). Replace the only degree-dependent factorial
quotient in (4) by its literal finite product:
\[
 T_{m,N}(x,\alpha)=
 \frac{P_N(w)S_{m-1}^{\,4}}
 {N^4 S_{2m-1}\prod_{h<m}(w-c_h)}
       \prod_{r=-m+1}^{m-1}2\sin\pi(x+r/N),
\]
\[
             \widehat\beta_N(x,\alpha)
                  =\sum_{m=1}^{M_N}T_{m,N}(x,\alpha).
 \tag{17}
\]
Thus no factorial interpolation in \(x\) is used.
At physical nodes these are exactly the first \(M_N\) terms of
(3). Positivity and (11), applied with \(b_0\), give
\[
 0\le \beta_{s,N}-\widehat\beta_N(s/N,\alpha)
 \le\frac{T_{1,N}(s/N,\alpha)q_{b_0}^{M_N}}{1-q_{b_0}},
 \qquad s/N\in[a,b].
 \tag{18}
\]
In particular the relative error is exponentially small, both
relative to \(\beta_{s,N}\) and to the prefix.

There is a fixed \(h_0>0\), independent of \(N,\alpha\), on which
the prefix and all its fixed \(x\)-derivatives are controlled.
Here and below one may reduce the real interval slightly from
\([a_0,b_0]\) while retaining a neighborhood of \([a,b]\).
Indeed its consecutive ratio is the entire-in-\(x\) expression
\[
 R_{m,N}(x,\alpha)=
 \frac{4s_m^4\{\sin^2(\pi x)-\sin^2(m\pi/N)\}}
 {(w-c_m)s_{2m}s_{2m+1}},\qquad m<M_N .
 \tag{19}
\]
On the real interval (14) applies even when \(Nx\) is not integral,
since \(m+1/2<Nx\) for all large \(N\). The coefficient of the
braces in (19) is bounded above by a constant independent of \(m,N\)
and real \(\alpha\), by the same sine calculation in (13).
The change of \(\sin^2(\pi x)\) under a small imaginary displacement
is uniformly \(O(|\Im x|)\). Shrink \(h_0\) so that, on a complex
rectangle containing \([a,b]\),
\[
                  |R_{m,N}(x,\alpha)|\le q_1<1
                    \qquad(m<M_N).
 \tag{20}
\]
We can also arrange \(|\sin^2(\pi x)|\le q_1\), enlarging \(q_1<1\)
if necessary. The real-part buffer and \(x-m/N>0\) in (16) keep
the individual prefix sine factors nonzero there.

The following leading coefficient makes the unit assertion precise.
For \(|z|<1\), define
\[
 \mathcal H_\alpha(z)=
 \sum_{\ell=0}^{\infty}z^\ell
 \prod_{j=1}^{\ell}
 \frac{j^3}{(j+\tfrac12)
          \{(j+\tfrac12)^2+(\alpha/(2\pi))^2\}},
 \tag{21}
\]
with empty product one, and put
\[
 \mathcal B_\alpha(x)=
 \frac{4\cosh^2(\alpha/2)\sin(\pi x)}
      {\pi(\alpha^2+\pi^2)}
               \mathcal H_\alpha(\sin^2\pi x).
 \tag{22}
\]
Every product factor in (21) lies in \((0,1)\) for real \(\alpha\).
The series is holomorphic for \(|z|<1\), uniformly for \(\alpha\)
in the fixed real compact interval. On real \(0<x<1/2\),
\(\mathcal B_\alpha(x)>0\).

**Theorem 2.** After reducing the fixed rectangle if necessary,
\[
       N\widehat\beta_N(x,\alpha)
            =\mathcal B_\alpha(x)+O_{\rm hol}(N^{-2}),
 \qquad
 \frac{c}{N}\le|\widehat\beta_N(x,\alpha)|\le\frac{C}{N}.
 \tag{23}
\]
Here \(c,C>0\) are uniform in (15). The holomorphic error notation
includes every fixed \(x\)-derivative on smaller fixed rectangles.

**Proof.** The first term is
\[
 T_{1,N}(x,\alpha)
 =\frac{4\cosh^2(\alpha/2)\,2\sin\pi x}
        {N^4(2\sin(\pi/N))
        \{2\cosh(\alpha/N)-2\cos(\pi/N)\}},
\]
so its normalized limit is the factor in front of \(\mathcal H\)
in (22), with uniform holomorphic error \(O(N^{-2})\).
The fixed-index limiting ratio of (19) is
\[
 r_m(x,\alpha)=
 \frac{m^3\sin^2(\pi x)}
 {(m+\tfrac12)\{(m+\tfrac12)^2+(\alpha/(2\pi))^2\}}.
 \tag{24}
\]
Taylor bounds for sine and cosh on the fixed compact ranges give
\[
 |R_{m,N}-r_m|\le C\frac{(m+1)^2}{N^2},
                         \qquad 1\le m<M_N .
 \tag{25}
\]
To check uniformity through this growing range, divide the sine
factors by their linear terms. On \(m/N\le\sigma<1/2\) these
quotients and their inverses are uniformly bounded, and their
errors from one are \(O((m+1)^2/N^2)\). Similarly
\[
 2\cosh(\alpha/N)-2\cos((2m+1)\pi/N)
 =\frac{\alpha^2+(2m+1)^2\pi^2}{N^2}
                  \{1+O((m+1)^2/N^2)\}.
\]
Its relative error and inverse are controlled uniformly because
the real denominator is positive and sine divided by its argument
is bounded below on that interval. Finally the numerator
\(\sin^2\pi x-\sin^2(m\pi/N)\) differs from \(\sin^2\pi x\)
by \(O(m^2/N^2)\). This proves (25).

Both ratio sequences have modulus at most a fixed \(q_1<1\).
Telescoping their \(\ell\)-fold products gives the error
\[
             C N^{-2}(\ell+1)^3 q_1^{\ell-1}.
 \tag{26}
\]
Summing this bound and the geometric tail after \(M_N-1\)
proves (23)'s expansion. The positive continuous function
\(\mathcal B_\alpha\) is bounded below on the real compact set
in (15). Its uniformly convergent series and continuity allow
a single smaller complex rectangle where it remains bounded away
from zero, uniformly in real \(\alpha\). The expansion proves
the two-sided bounds in (23). Cauchy's formula on a larger fixed
rectangle proves the stated derivative bounds. \(\square\)

Thus the positive coefficient has zero extensive action on this
bulk interval: after multiplying by \(N\), it has a nonzero bounded
analytic limit. This assertion excludes the checkerboard in (3).

## 4. One exact analytic interpolation

The exponentially accurate prefix can be made exact without a new
extensive phase. This is the localized sinc method of the pinned
physical-row interpolation source, here with zero action in the
amplitude. We give the estimate in this simpler normalization.

Let \(s_0=\lceil Na\rceil\), \(s_1=\lfloor Nb\rfloor\), and
\[
 d_{s,N}(\alpha)=
          \beta_{s,N}(\alpha)-\widehat\beta_N(s/N,\alpha).
\]
By (18) and (23), there are \(C,\kappa>0\) such that
\[
                    |d_{s,N}|\le C N^{-1}e^{-\kappa N}.
 \tag{27}
\]
For example, decreasing an exponent if needed, one can take
\(\kappa=\sigma|\log q_{b_0}|/2\).
Define the finite analytic function
\[
 \mathfrak b_N(x,\alpha)=\widehat\beta_N(x,\alpha)
  +\sum_{s=s_0}^{s_1}d_{s,N}(\alpha)
       \operatorname{sinc}(Nx-s)e^{-N(x-s/N)^2},
 \qquad
 \operatorname{sinc}z=\frac{\sin\pi z}{\pi z}.
 \tag{28}
\]
The removable value at zero is one. Hence
\[
               \mathfrak b_N(s/N,\alpha)=\beta_{s,N}(\alpha)
                    \quad(s_0\le s\le s_1).
 \tag{29}
\]
Choose a fixed strip half-height
\[
 0<H\le
 \min\{h_0/2,\ \kappa/(8\pi),\ \sqrt{\kappa/8}\},
 \tag{30}
\]
inside the rectangle where (23) holds, with a fixed real enlargement
of \([a,b]\) still included. If \(x=X+iY\), then
\[
 |\operatorname{sinc}(Nx-s)|\le e^{\pi N|Y|},\qquad
 |e^{-N(x-s/N)^2}|
       =e^{-N(X-s/N)^2+NY^2}.
 \tag{31}
\]
The first inequality follows from
\(\operatorname{sinc}z=\tfrac12\int_{-1}^{1}e^{i\pi zu}\,du\).
There are at most \(N\) summands. Dividing their absolute bound
by the lower bound \(c/N\) in (23) gives
\[
 \left|\frac{\mathfrak b_N}{\widehat\beta_N}-1\right|
 \le CN\exp\{-N(\kappa-\pi|Y|-Y^2)\}
                       \le C e^{-\kappa N/2}.
 \tag{32}
\]
Consequently \(\mathfrak b_N\) is a holomorphic unit on this fixed
strip for all sufficiently large \(N\), and
\[
 N\mathfrak b_N(x,\alpha)
      =\mathcal B_\alpha(x)+O_{\rm hol}(N^{-2}),\qquad
               c/N\le|\mathfrak b_N|\le C/N .
 \tag{33}
\]
Every fixed derivative of the relative error in (32) has the same
exponential bound on a smaller fixed strip, by Cauchy. The physical
values (29) are exact, not asymptotic.

The actual signed coefficient is interpolated by
\[
                    -\eta e^{i\pi Nx}\mathfrak b_N(x,\alpha),
 \tag{34}
\]
since its value at \(x=s/N\) is (3). Its checkerboard character
has not been absorbed into the bounded amplitude or discarded.
For example, for any holomorphic spectator \(f\) and a positively
oriented contour \(\Gamma\) in this strip enclosing exactly
\(s_0/N,\ldots,s_1/N\),
\[
 \sum_{s=s_0}^{s_1}b_{N-s,N} f(s/N)
 =\frac1{2\pi i}\int_\Gamma
 \frac{2\pi iN}{e^{2\pi iNx}-1}
       [-\eta e^{i\pi Nx}\mathfrak b_N(x,\alpha)]f(x)\,dx .
 \tag{35}
\]
The sampling kernel has residue one at every displayed degree node.
Its aliases, the checkerboard, the spectator, and all connector
integrals remain in this identity.

## 5. Scope and direct-source readbacks

The original ordinary polynomial was used throughout Proposition 1.
Thus both parities, including the odd simple physical node, and
every physical first normal are retained automatically. The degree
variable \(x\) in (28) is an interpolation variable; its derivative
is not being substituted for a spectral normal.

The theorem concerns a single endpoint kernel and the coefficients
with \(s/N\) in a fixed compact subinterval of \((0,1/2)\).
It gives no uniform endpoint or fold limit. Fourier coefficients
of shared products require their actual convolutions and are not
identified with (3). Real bounded \(\alpha\) is the parameter
range proved here; no complex-\(\alpha\) unit assertion is needed.
Neither positivity of \(\beta\) nor the moderate interpolation
estimates the joined central, outer, and vertical source.
In particular (35) does not suppress the external degree connectors
or imply a filled-action upper bound or scalar noncancellation.

The ordinary endpoint bounds and the general localized interpolation
method are earlier results. The new input is the exact signed
positive Fourier sum, its uniform bulk contraction, and the
explicit nonzero analytic symbol for these actual coefficients.
The full texts of the following direct sources were read at the
displayed matching versions, and their used implications checked:

* [Original edge kernel and physical polynomial](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_edge_kernel_difference_and_endpoint_bound.md),
  SHA256 5d0d07d4d97d82cca66e0e0c3bf2cecad8e5f58ef8329178278b297cf0d6c5da:
  ordinary Newton normalization and exact physical polynomial (1).
* [Coherent full endpoint kernel](research_full_period_endpoint_kernel_reduction.md),
  SHA256 a1d67ac803c0160bbfdacaa96a6fde9dc1ffae06fc39eb94f0416dcf2ecef76e:
  placement as the original ordinary endpoint kernel, with its
  low sector and full radical both retained.
* [Exact moderate degree interpolation](research_physical_row_analytic_degree_interpolation.md),
  SHA256 f7d673e6633c0f46498a6c023512a3c64724d35c53ea168dabbd7f1e59f72d51:
  the single-strip Gaussian-localized sinc construction and its
  relative-error budget, specialized and proved in Section 4.

Only written proofs, text reads, and hashes were used. No mathematical
program, numerical experiment, test, or compilation was run.
Previously frozen notes and public manuscripts are unchanged.
