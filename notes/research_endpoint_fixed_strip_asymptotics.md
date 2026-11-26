# Endpoint asymptotics on a fixed complex neighborhood

Private written proof, 16 November 2026.

The bulk value formula extends to a fixed, sufficiently thin complex
neighborhood after reducing its power saving. Combined with the exact
scalar compatibility theorem, this gives an asymptotic formula for
one representative of the actual values and first spectral derivatives.
At the complete endpoint its leading factor is a holomorphic unit.
The same remains true in a specified shrinking neighborhood of that
endpoint. This is a local statement; it does not supply the coefficient
of a geometric cycle in the whole original trace.

## 1. A quantitative continuation lemma

Let \(a<b\), \(H>0\), and let \(r_N\) be holomorphic on a neighborhood
of the closed rectangle
\[
             a\le\Re z\le b,\qquad |\Im z|\le H.
\]
Suppose, uniformly in any additional real parameters,
\[
 |r_N(z)|\le C N^P,\qquad
 |r_N(x)|\le C N^{-q}\quad(a\le x\le b),
 \qquad P\ge0,\quad q>0.                                    \tag{1}
\]
Enlarge the common constant \(C\) if necessary. Fix
\(0<d<(b-a)/2\) and \(0<\lambda<q\). Set
\[
 B=\frac1H+\frac4{\pi d},\qquad
 h=\min\left\{\frac H2,\frac{\lambda}{B(P+q)}\right\}.
                                                               \tag{2}
\]
Then
\[
 |r_N(x+iy)|\le C N^{-q+\lambda}
 \quad(a+d\le x\le b-d,\ |y|\le h).                          \tag{3}
\]
On any smaller rectangle, every fixed complex derivative has the
same bound, with a derivative-dependent constant.

Here is a direct barrier proof. In the upper rectangle define
\[
 w(x,y)=\frac yH+\frac2\pi
       \left\{\arctan\frac y{x-a}
                    +\arctan\frac y{b-x}\right\}.            \tag{4}
\]
The two arctangents are arguments of nonvanishing linear functions
in their respective half-planes; both are harmonic. Thus \(w\) is
harmonic. It vanishes on the open bottom edge, is at least one on
each other edge, and is nonnegative. The subharmonic function
\[
 \log|r_N|-\log C+q\log N-(P+q)(\log N)w
\]
has nonpositive boundary upper limits. At a bottom corner this also
holds by continuity of \(r_N\), since its value there satisfies the
second bound in (1). The maximum principle therefore gives
\[
                  |r_N(x+iy)|
                      \le C N^{-q+(P+q)w(x,y)}.              \tag{5}
\]
For the indicated buffered real parts,
\[
 w(x,y)\le y\left(\frac1H+\frac2\pi
             \left\{\frac1{x-a}+\frac1{b-x}\right\}\right)
          \le By .
\]
This proves (3) above the real axis; reflection gives the lower
half. Cauchy's formula on fixed-radius disks in a smaller
rectangle proves the derivative assertion. Zeros of \(r_N\)
are harmless in the subharmonic argument.

In particular, if \(q=1+\epsilon\), a fixed strip can retain the
bound \(O(N^{-1-\epsilon/2})\), by taking
\(\lambda=\epsilon/2\). A strip of width \(1/\log N\) is useful
for keeping the original exponent without loss; it is unnecessary
when a smaller positive power saving suffices.

## 2. The actual endpoint representative

Retain the original notation
\[
 \begin{gathered}
 c_j=2\cos((2j+1)\pi/N),\qquad
 c_N(x)=2\cos(2\pi x+\pi/N),\\
 w_N(\alpha)=2\cosh(\alpha/N),\qquad
 K_N(w,Z)=\sum_{k=0}^{N-1}e_k(w)e_k(Z),\\
 S_N(x)=\frac N\pi\sin(\pi x).
 \end{gathered}                                             \tag{6}
\]
The \(e_k\) are the original normalized Newton polynomials. Fix a
closed interval \(I\Subset(0,1/2)\) and a compact real parameter
interval \(|\alpha|\le A\). The scalar compatibility theorem supplies,
on a fixed complex neighborhood of a slightly larger real interval,
a polynomially bounded holomorphic function \(h_N(x,\alpha)\)
with
\[
 \begin{split}
 h_N(j/N,\alpha)&=K_N(w_N(\alpha),c_j),\\
 \partial_xh_N(j/N,\alpha)
     &=c_N'(j/N)\partial_ZK_N(w_N(\alpha),c_j).
 \end{split}                                               \tag{7}
\]
It is jointly holomorphic in bounded complex endpoint parameters.
For the asymptotic assertion below the parameters are real.

Put \(\nu=\alpha/\pi\), and set
\[
 k_\pm(\nu)=\frac{\Gamma(\pm i\nu)}
                        {\Gamma(1/2\pm i\nu/2)^4},\quad
 C_0(\nu)=k_+(\nu)+k_-(\nu),\quad
 C_1(\nu)=i\nu(k_+(\nu)-k_-(\nu)).                            \tag{8}
\]
The two \(C_i\) are regular and even at zero, with
\[
 C_0(0)=\frac{2(\gamma_E+4\log2)}{\pi^2},
                  \qquad C_1(0)=\frac2{\pi^2}.
\]
Define, using the removable value of \(\sin(\nu\log s)/\nu\),
\[
 g_\alpha(s)=\frac1s
       \left\{C_0(\nu)\cos(\nu\log s)
                      +C_1(\nu)\frac{\sin(\nu\log s)}{\nu}\right\}.
                                                               \tag{9}
\]
For \(s=S_N(x)\), choose \(\log\sin(\pi x)\) to be real on the
real interval. It has a single holomorphic branch on a sufficiently
small fixed neighborhood of that interval.

**Theorem 1.** There exist a fixed complex neighborhood \(U\) of
\(I\) and \(\epsilon_*>0\) such that, for real \(|\alpha|\le A\),
\[
 h_N(x,\alpha)=g_\alpha(S_N(x))+O(N^{-1-\epsilon_*})
                                                     \quad(x\in U).
                                                               \tag{10}
\]
The error is holomorphic in \(x\). Every fixed \(x\)-derivative has
the same bound on smaller fixed neighborhoods. Both level parities
are included. The neighborhood can be thin, and its size is not a
claim about the location of a geometric critical point.

*Proof.* The value connection theorem applies to \(h_N\), since it
is a moderate exact value interpolation. On a buffered real interval
containing \(I\) it gives
\[
                h_N(x,\alpha)-g_\alpha(S_N(x))
                                  =O(N^{-1-\epsilon})         \tag{11}
\]
for some \(\epsilon>0\), uniformly for the stated real parameters.
On a fixed larger rectangle \(h_N\) has a bound \(CN^P\).
On that same rectangle the second term is
\(O_A((1+\log N)/N)\): the imaginary part of \(\log S_N(x)\)
is bounded, \(\nu\) is real and bounded, and the removable expression
in (9) costs at most \(C_A(1+\log N)\).
Thus their difference satisfies (1), with \(q=1+\epsilon\)
and some \(P\ge0\). Apply (2)--(3) with
\(\lambda=\epsilon/2\), then shrink the rectangle to retain
fixed derivative buffers. This proves (10) with
\(\epsilon_*=\epsilon/2\). No off-real small-error estimate from
the value theorem was assumed. \(\square\)

At the physical nodes, (7) and (10) give the actual spectral
derivative, by division by
\[
                  c_N'(x)=-4\pi\sin(2\pi x+\pi/N),
\]
which is uniformly nonzero on a smaller fixed bulk neighborhood.
Thus the result does not concern a substitute derivative obtained
by moving recurrence coefficients.

## 3. A nonzero factor near the complete endpoint

Write \(\operatorname{sinc}u=\sin u/u\), with
\(\operatorname{sinc}0=1\). Let \(\beta\) be real and range over
a fixed bounded interval, and put
\[
                     \alpha_N=\frac{\beta}{\log N}.
\]
On the fixed complex neighborhood from Theorem 1,
\[
 h_N(x,\alpha_N)=
       \frac{2\log N}{\pi N\sin(\pi x)}
                      \operatorname{sinc}(\beta/\pi)
                          +O(N^{-1}).                       \tag{12}
\]
All fixed \(x\)-derivatives have the same additive error on smaller
neighborhoods, uniformly for bounded real \(\beta\).

To prove this, put
\(\lambda(x)=\log(\sin(\pi x)/\pi)\), so
\(\log S_N(x)=\log N+\lambda(x)\).
In (9), \(\nu=\beta/(\pi\log N)\), and analyticity at zero gives
\[
 \begin{split}
 C_0(\nu)&=C_0(0)+O((\log N)^{-2}),\\
 C_1(\nu)&=2/\pi^2+O((\log N)^{-2}),\\
 \frac{\sin(\nu\log S_N(x))}{\nu}
      &=(\log N)\operatorname{sinc}(\beta/\pi)
                    +\lambda(x)\cos(\beta/\pi)
                    +O((\log N)^{-1}).
 \end{split}
\]
The last expansion is uniform also at \(\beta=0\), by its entire
power series. Substitution proves (12), including the derivative
bounds.

If \(|\beta|\le B<\pi^2\), the real factor
\(\operatorname{sinc}(\beta/\pi)\) is positive and bounded away
from zero. Consequently
\[
 h_N(x,\beta/\log N)=
       \frac{2\log N}{\pi N\sin(\pi x)}
             \operatorname{sinc}(\beta/\pi)
                    \{1+O_{\mathrm{hol}}((\log N)^{-1})\}.   \tag{13}
\]
For all large \(N\) this is a holomorphic unit on a smaller
neighborhood. At \(\beta=0\) it applies to the complete endpoint
\(w_N(0)=2\).

For any fixed number \(r\) of factors sharing the same variable,
their ordinary product therefore satisfies
\[
 \prod_{i=1}^r h_N(x,\beta_i/\log N)
 =\left(\frac{2\log N}{\pi N\sin(\pi x)}\right)^r
     \prod_{i=1}^r\operatorname{sinc}(\beta_i/\pi)
                       \{1+O_{\mathrm{hol}}((\log N)^{-1})\}, \tag{14}
\]
uniformly for \(|\beta_i|\le B<\pi^2\).
It retains the original shared first normal by the product rule
and (7). The analogous product over finitely many variables
retains every mixed first normal. No spectral variable is reduced
before its actual closing functional is applied.

For fixed nonzero real \(\alpha\), Theorem 1 still applies, but
the leading expression (9) oscillates in \(\log N\). Equation
(13) is not extended to those parameters. In particular no
nonvanishing assertion is made at the first zeros
\(\beta=\pm\pi^2\).

## 4. What this proves for a local saddle integral

There is a useful precise consequence of (14). Suppose a particular
local contour through a nondegenerate critical point \(z_*\), in
the product of the neighborhoods above, has already been chosen
for a bare source. Suppose its local integral has the form
\[
 I_N=e^{N\Phi(z_*)}N^{-d/2}\{A_*+o(1)\},\qquad A_*\ne0,    \tag{15}
\]
and its integrand \(a_N(z)e^{N\Phi(z)}\,dz\) obeys the usual
absolute Gaussian estimate on that contour:
in real local coordinates \(u\),
\[
 |a_N(z(u))\,dz|\le C\,du,\qquad
 \Re(\Phi(z(u))-\Phi(z_*))\le-c|u|^2.
                                                               \tag{16}
\]
The parametrization is Lipschitz near zero; the fixed local
contour has no other point of equal real phase. Polynomial scalar
prefactors can be taken outside (15).

Insert the products in (14), with total number of factors \(r\).
After dividing them by \((\log N/N)^r\), write the multiplier as
\(b_N(z)\). Equation (14) gives
\[
 b_N(z)=b(z)+O_{\mathrm{hol}}((\log N)^{-1}),\quad
 b(z)=\left(\frac2\pi\right)^r
       \prod_v\sin(\pi x_v)^{-r_v}
       \prod_i\operatorname{sinc}(\beta_i/\pi).              \tag{17}
\]
Here \(r_v\) counts factors at variable \(x_v\), and
\(\sum_v r_v=r\). On compact sets \(b(z_*)\ne0\), uniformly for
the indicated real parameters. It follows that the decorated
local integral equals
\[
 \left(\frac{\log N}{N}\right)^r
 e^{N\Phi(z_*)}N^{-d/2}\{b(z_*)A_*+o(1)\}.                \tag{18}
\]

Indeed
\[
 |b_N(z(u))-b(z_*)|\le C\{(\log N)^{-1}+|u|\}.
\]
Multiplying by (16) and integrating bounds the difference from
\(b(z_*)I_N\) by
\[
 C e^{N\Re\Phi(z_*)}N^{-d/2}
                        \{(\log N)^{-1}+N^{-1/2}\}.
\]
This proves (18) directly from the stated local hypotheses. In
particular these endpoint factors cannot make that already
specified local Gaussian coefficient zero.

This consequence does not supply (15), choose a contributing
contour, or show that \(z_*\) lies in the thin neighborhood furnished
by Theorem 1. Nor does it exclude cancellation with another part
of the original closed sum. The full trace retains its outer
vertical integrals and complementary physical rows.

## 5. Direct sources and scope

The complete source proofs were read at these unchanged versions,
and their used implications and hashes checked:

* [Scalar compatibility](research_microscopic_endpoint_bulk_scalar_compatibility.md),
  SHA256 2b8713ed16b66f5faa004403ac1d032021eee0a6f8f38082481d002c672c0b2e:
  a polynomially bounded scalar matching the actual values and
  spectral normals, including bounded complex endpoint parameters.
* [Value connection and overlap](research_endpoint_value_connection_and_overlap.md),
  SHA256 87801bd8baca255a86fdbcd5170662fd9f2b366f983507f776d5676fd8a324da:
  the explicit \(C_0,C_1\), their removable zero-parameter values,
  and the uniform real-interval error for any moderate exact
  value interpolation.

The additional arguments here are the explicit fixed-strip barrier,
the shrinking-parameter unit formula, and its local multiplier
consequence. They give neither a whole-source exponential bound
nor the finite-exception filling theorem. Only written mathematics,
source-text reads and hashes were used; no numerical experiment,
mathematical program, test or build was run. Frozen manuscripts
and public documentation remain unchanged.
