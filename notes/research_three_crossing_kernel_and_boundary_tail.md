# A finite kernel sum and the retained terminal endpoint sector

Research note, 3 November 2026.

The normal-ordered identity kernel has a single finite product-sum
formula. Its central forcing cancels only after the complete cyclic
iteration. Separately, the high-degree half of an original terminal
polynomial has a nonzero asymptotic off the physical interval, uniform
over every signed integer crossing power. That entire sector can
nevertheless have only polynomial size after an original closing
twist. These statements identify a contribution which a joint contour
must retain; they do not give a full terminal or adjacent-pair packet.

## 1. A finite product formula for the identity kernel

Use \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(\eta=(-1)^D\), and the original Newton basis \(e_\ell\).
Write \(P_N(w)=2T_N(w/2)+2\).
The polynomials \(h_\ell=e_\ell(\mathcal D_3)1\), with
\[
 \mathcal D_3F(X)
     =qXF(X)+q^{-1}X^{-1}\{F(X)-F(Q^{-1}X)\},
 \tag{1}
\]
and the identity kernel
\[
 \mathcal I_N(X,w)
       =\sum_{\ell=0}^D e_\ell(w)h_{D-\ell}(X)
 \tag{2}
\]
are those of the
[full boundary-current theorem](research_three_crossing_boundary_current.md),
Section 2. In particular \(\mathcal I_N\) is an ordinary
polynomial of degree at most \(D\) in either variable.

For a nonzero \(t\), put \(w=t+t^{-1}\), and use the finite
product \((z;Q)_m=\prod_{r=0}^{m-1}(1-zQ^r)\).

**Theorem 1.** The following is an ordinary polynomial identity:
\[
 \boxed{\quad
 \mathcal I_N(X,t+t^{-1})
   =-\frac{\eta qQ}{N^2}\,X^{1-N}
       \sum_{m=0}^{N-1}Q^m
           (qQtX;Q)_m(qQt^{-1}X;Q)_m .
 \quad}                                                         \tag{3}
\]
The numerator on the right is divisible by \(X^{N-1}\),
coefficientwise as a polynomial in \(w\). Thus the apparent pole
at \(X=0\) is removable. There is no infinite product or convergence
condition on \(X,t\).

*Proof.* The full top-degree identity is
\[
 (w-\mathcal D_3)\mathcal I_N
        =\frac{\eta}{N^2}\{P_N(w)+X^N-2\}.
 \tag{4}
\]
Let
\[
 a_w(X)=(1-qtX)(1-qt^{-1}X),\qquad
 K_0=P_N(w)+X^N-2.
 \tag{5}
\]
Multiplication of (4) by \(qX\) gives
\[
 \mathcal I_N(Q^{-1}X,w)
    =a_w(X)\mathcal I_N(X,w)+\frac{\eta q}{N^2}XK_0 .
 \tag{6}
\]
The forcing \(K_0\) is unchanged by the clock shift. Moreover
\[
 \begin{split}
 \prod_{j=0}^{N-1}a_w(Q^{-j}X)
  &=(1+t^NX^N)(1+t^{-N}X^N)\\
  &=1+X^NK_0.
 \end{split}                                                    \tag{7}
\]
Iterating (6) exactly \(N\) times therefore gives
\[
 -X^NK_0\,\mathcal I_N(X,w)
   =\frac{\eta q}{N^2}XK_0
       \sum_{j=0}^{D}Q^{-j}
                   \prod_{r=j+1}^{D}a_w(Q^{-r}X).
 \tag{8}
\]
First cancel on the open set \(XK_0\ne0\).
Reindexing by \(m=D-j\) turns the finite sum into
\[
 Q\sum_{m=0}^{D}Q^m
                     (qQtX;Q)_m(qQt^{-1}X;Q)_m.
 \tag{9}
\]
This proves (3) there. Since the left side is the polynomial
(2), the numerator is divisible by \(X^D\) and the identity
extends to all \(X,w\). The symmetry under \(t\leftrightarrow
t^{-1}\) also follows term by term. In particular the
cancellation in (8) is not permission to remove the forcing
before the cyclic iteration. \(\square\)

Formula (3) computes the first component of the two-state
calculus. The original turn kernel is obtained by reversing its
Newton coefficients in \(w\); its actual source also contains the
second-state current. The two-spectra splitting in the cited note
shows explicitly why the primary kernel alone does not determine
the original source asymptotic.

## 2. The full high-degree endpoint sector

For every signed integer \(p\), let
\[
 \alpha_{p,j}=(M^p\mathbf e_0)_j,\qquad
 H_{p,N}(w)=T(R^p)(w)
                   =\sum_{j=0}^D\alpha_{p,j}e_{D-j}(w).
 \tag{10}
\]
The crossing scalar is
\(\kappa=\exp(\pi iD^2/(2N))\).
Retain the entire distinct-node half of these original
coefficients:
\[
 m_N=\left\lfloor\frac{N-1}{2}\right\rfloor,\qquad
 E_{p,N}(w)=\sum_{j=0}^{m_N}\alpha_{p,j}e_{D-j}(w).
 \tag{11}
\]
This is a specified ordinary polynomial summand of \(H_{p,N}\).
It is not a different trace model, and its boundary derivatives
are those of the displayed polynomial.

**Theorem 2.** On every compact subset \(K\) of
\(\{w\in\mathbb C:|\operatorname{Im}w|>1\}\),
\[
 \boxed{\quad
 E_{p,N}(w)=\kappa^p e_D(w)\{1+\varepsilon_{p,N}(w)\},
 \qquad
 \sup_{w\in K}|\partial_w^r\varepsilon_{p,N}(w)|
                       =O_{K,r}(N^{-2})
 \quad}                                                         \tag{12}
\]
for every fixed nonnegative integer \(r\), uniformly over all
signed integers \(p\). The power \(p\) may depend on \(N\).
In particular this sector is nonzero on \(K\) for sufficiently
large \(N\).

*Proof.* The reflected sine products give exactly
\[
 S_jS_{D-j}=N,\qquad c_{D-r}=c_r,\qquad
 \frac{e_{D-j}(w)}{e_D(w)}
       =\frac{S_j^2}{\prod_{r=1}^j(c_r-w)}.
 \tag{13}
\]
Here \(S_j=\prod_{r=1}^j2\sin(\pi r/N)\). The last identity
also holds at \(j=0\), with empty products one.
All zeros of \(e_D\) are real, so this quotient is holomorphic
throughout the domain under consideration.
Since \(\alpha_{p,0}=\kappa^p\), (13) expresses the relative
error in (12) as the sum of the terms \(j\ge1\).

The [original low-color bound](research_original_low_color_bound.md)
gives, uniformly in \(p\),
\[
 \begin{split}
 |\alpha_{p,j}|&\le\sqrt2
       &&\left(j\le\left\lfloor\frac{N-2}{4}\right\rfloor\right),\\
 |\alpha_{p,j}|&\le\csc\frac{\pi}{2N}\le N
       &&(0\le j\le m_N).
 \end{split}                                                    \tag{14}
\]
The second line includes the final simple node at odd levels.
Also \(S_j^2\le2N\) throughout this half: its consecutive
ratios first lie below one and then above one, and its final
value is at most \(2N\).

Choose a slightly larger compact neighborhood of \(K\) still
in the same domain, and put \(\rho=\inf|\operatorname{Im}w|>1\)
on that neighborhood. Choose a fixed \(0<\delta<1/4\) with
\(4\sin^2(\pi\delta)<\rho/2\). For \(1\le j\le\delta N\),
\[
 \frac{S_j^2}{\rho^j}
      \le \frac{S_1^2}{\rho}\,2^{1-j}.
 \tag{15}
\]
The first line of (14) bounds the sum of these terms by
\(O(N^{-2})\). For the remaining indices use
\[
 |\alpha_{p,j}|\,\frac{S_j^2}{\rho^j}
                  \le 2N^2\rho^{-j}.
 \tag{16}
\]
Their geometric sum is exponentially small. This proves (12)
for \(r=0\), uniformly on the larger neighborhood.
Cauchy's formula then proves every fixed derivative estimate
on \(K\), with constants still independent of \(p\). \(\square\)

The leading term is completely specified:
\[
 e_D(w)=\frac{\eta P_N(w)}{N^2(w-c_0)}.
 \tag{17}
\]
If \(w=-2\cos u\), with \(u\) in a compact complex set whose
image satisfies \(|\operatorname{Im}w|>1\), then
\[
 P_N(-2\cos u)=2+2(-1)^N\cos(Nu),\qquad
 \frac1N\log|E_{p,N}(-2\cos u)|
                         \longrightarrow|\operatorname{Im}u|
 \tag{18}
\]
uniformly on that set and uniformly in \(p\).
The image condition keeps \(|\operatorname{Im}u|\) bounded
away from zero. This result concerns the sector (11);
it does not rule out its cancellation against the remaining
colors of the full terminal polynomial.

## 3. A polynomial original closing despite off-real growth

The same sector has a simple exact closing formula. The trace
\(\phi_N\) is the original top Newton coefficient, with all
double-root normal data retained.

**Corollary 3.** For arbitrary signed integers \(a,p\),
\[
 \boxed{\quad
 \phi_N(R^aE_{p,N})
       =\sum_{j=0}^{m_N}\alpha_{a,j}\alpha_{p,j},
 \qquad
 |\phi_N(R^aE_{p,N})|\le\frac76N^2 .
 \quad}                                                         \tag{19}
\]
The bound is uniform even when \(a,p\) depend on \(N\).
There is no complex conjugation in this bilinear formula.

*Proof.* The full original turn identity
\(JM^aJ=(M^a)^T\) gives
\[
 \phi_N(R^a e_{D-j})
       =(M^a)_{D,D-j}
       =(M^a)_{j,0}=\alpha_{a,j}.
 \tag{20}
\]
This proves the equality in (19) before taking absolute
values.
For even \(N\), the squared coefficient bound from the
low-color theorem has sum at most
\[
 \cos^2\frac{\pi}{2N}
   \sum_{j=0}^{N/2-1}
       \sec^2\frac{(j+1/2)\pi}{N}
                  \le\frac{N^2}{2}.
 \tag{21}
\]
For odd \(N=2m+1\), the first \(m\) bounds and the final
distinct-node bound give
\[
 \cos^2\frac{\pi}{2N}\frac{N^2-1}{6}
           +\csc^2\frac{\pi}{2N}
                         \le\frac76N^2.
 \tag{22}
\]
The identities used here are
\(\sum_{r=1}^{N-1}\csc^2(r\pi/N)=(N^2-1)/3\) and
\(\sum_{r=0}^{N-1}\csc^2((r+1/2)\pi/N)=N^2\).
They follow by taking two logarithmic derivatives of the
finite sine-product formula; symmetry gives the half sums.
Bounding each product
\(|\alpha_{a,j}\alpha_{p,j}|\) by the corresponding squared
bound proves (19). \(\square\)

Thus an entire original sector of rate
\(|\operatorname{Im}u|\) off the real interval can have only
polynomial size after a closing twist. This is a concrete
coherent estimate for that closing operation, not an
inference from an absolute off-real tail bound.
An additional free-boundary kernel or prepared exterior
does not satisfy the hypotheses of (20), so (19) does not
by itself control the \((-3,-3)\) pendant or a longer word.
The full two-state current remains necessary in those
compositions.
