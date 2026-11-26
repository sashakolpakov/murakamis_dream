# A complete-trace bound for the next-three dual source

Research deduction, 7 November 2026. The exact lowered-word identity
expresses the next \(343\) source as an inverse-crossing observation
of the ordinary \(33\) kernel and the original endpoint polynomial.
This note gives an explicit bound for that whole observation and
its exact angular contour, including the endpoint current.

The polynomial-cost trace estimate is the specialization of
[calibrated finite gluing, Lemma 1](research_calibrated_remainders_under_finite_gluing.md),
not a new general gluing theorem. The source-specific input here is
the complete endpoint polynomial on a disk and the exact cancellation
of the old factorial. No comparison with the new action is assumed,
and no numerical evaluation is used.

## 1. Degree dependence and all physical normals

Retain \(D=N-1\), \(q=e^{\pi i/N}\), \(r=q^{-2}\),
\(\kappa=q^{D^2/2}\), and the original full trace \(\phi_N\).
For a polynomial \(B(t)\), write
\(\|B\|_{\rm real}=\sup_{-2\le t\le2}|B(t)|\).
For every integer \(n\) and every polynomial \(B\) of degree
at most \(L\), the unreduced-product estimate is
\[
 \boxed{\quad
 |\phi_N(R_N^nB)|
       \le \left\{N(L+1)+\frac{|n|N^2}{2}\right\}
                                      \|B\|_{\rm real}.
 \quad}                                                        \tag{1}
\]
The right side concerns the displayed polynomial \(B\), whose
degree need not be below \(N\). No supremum of the canonical
remainder of \(R_N^nB\) is substituted.

For a direct check of all normals, use the derivative-sampling
formula in
[the exact complete trace, equations (1)--(5)](research_exact_complete_trace_contour.md).
For the even trigonometric polynomial \(b(\theta)=B(-2\cos\theta)\),
put
\[
 \begin{split}
 \eta&=(-1)^D,\qquad C_{N,n}=q^{nD^2/4},\\
 \tau_j&=\frac{2\pi}{N}(D/2-j),\quad 0\le j<N,\\
 g_n(\theta)&=\sin\theta\,b(\theta)
                             e^{inN\theta^2/(4\pi)}.
 \end{split}                                                   \tag{2}
\]
Then
\[
 \phi_N(R_N^nB)=\eta C_{N,n}\sum_{j=0}^{N-1}g_n'(\tau_j).
 \tag{3}
\]
The exponential has modulus one on this real grid.
Trigonometric Bernstein gives
\(\|b'\|_{\mathbb R}\le L\|b\|_{\mathbb R}
=L\|B\|_{\rm real}\). The three terms in \(g_n'\) are bounded
respectively by \(1,L,|n|N/2\) times this norm.
Summing proves (1). The two grid points at each double spectral
root retain its value and first derivative. At odd levels
\(\tau=0\) gives \(g_n'(0)=B(-2)\), the required simple-root
term. Thus the same bound applies at both parities.
For \(N=2\) the same estimate follows from the full Hermite
formula in [twist tomography, equations (3)--(5)](research_original_twist_observation_tomography.md);
only \(N\ge3\) is needed for the contour statements below.

Equivalently the physical double-root formula contains
\[
 \lambda_j^n
   \{d_jB'(c_j)+(n d_j\alpha_j-c_j)B(c_j)\},
 \quad
 |\lambda_j|=1,\quad d_j=4\sin^2\theta_j,\quad
 d_j\alpha_j=i(D-2j)\sin\theta_j .
 \tag{4}
\]
In particular the normal of the inverse crossing is retained
when \(n=-1\). A unit-modulus bound for its values alone would
not prove (1).

## 2. A disk bound for the complete endpoint polynomial

Use the original polynomial
\[
 H_N(t,W)=\sum_{\ell=0}^{D}
          \frac{(-q)^{-\ell}e_\ell(t)}{P_\ell}(W;r)_\ell .
 \tag{5}
\]
It has separate degrees at most \(D\) in \(t,W\).
The coherent seam estimate, including its all-real-color extension
in [terminal real-color decay, Lemma 2](research_mixed_terminal_real_color_decay.md),
says that for every \(\tau>0\),
\[
 \sup_{t\in[-2,2]}\sum_{j=0}^{D}
         |H_N(t,r^{-j})|
        \le C_\tau N^{a_\tau}e^{N(b_0+\tau)},
 \qquad b_0=101/125 .
 \tag{6}
\]
This is a sum of whole coherent endpoint coefficients. Its proof
includes both physical ends and all real ordinary colors.

The degree-\(D\) cardinal identity is
\[
 H_N(t,W)=\frac1N\sum_{j=0}^{D}H_N(t,r^{-j})
                         \sum_{\nu=0}^{D}(Wr^j)^\nu .
 \tag{7}
\]
Each cardinal factor has modulus at most one on the closed unit
disk. For \(|W|\ge1\), the reciprocal-polynomial maximum principle
adds at most the factor \(|W|^D\). Consequently
\[
 \boxed{\quad
 \sup_{\substack{t\in[-2,2]\\ |W|\le R}}
     |H_N(t,W)|
   \le C_\tau N^{a_\tau}
                e^{N\{b_0+\log_+R+\tau\}} .
 \quad}                                                        \tag{8}
\]
Here \(R\ge0\) is bounded, and \(\log_+0=0\).
Every original numerator zero is retained. No endpoint packet is
continued to an unproved complex private-index domain.

The same estimate holds with polynomial cost for fixed
\(W\)-derivatives: use Cauchy's formula on a radius \(N^{-1}\)
around a point in \(|W|\le R\), and apply (8) at \(R+N^{-1}\).
The change in \(N\log_+R\) is bounded independently of \(N\).
Fixed real ordinary \(t\)-derivatives follow from Markov's
inequality on the full ordinary polynomial before any positive
summation.

## 3. A whole signed observation and a concrete remainder rule

For a polynomial \(A_N(t)\) of degree at most \(L_N\), define
\[
 \mathfrak O_{n,N}[A_N](Z)
        =\phi_N^{(t)}
             [R_N(t)^n A_N(t)H_N(t,rZ)].
 \tag{9}
\]
The inverse crossing means its original quotient element. Equations
(1) and (8), applied to the unreduced product of degree at most
\(L_N+D\), prove
\[
 \boxed{\quad
 \sup_{|Z|\le R}|\mathfrak O_{n,N}[A_N](Z)|
  \le C_\tau N^{a_\tau}
      \left\{N(L_N+N)+\frac{|n|N^2}{2}\right\}
      \|A_N\|_{\rm real}
          e^{N\{b_0+\log_+R+\tau\}} .
 \quad}                                                        \tag{10}
\]
Thus \(L_N=O(N)\) and a fixed signed \(n\) cost no additional
exponential factor. This is a bound for the complete prescribed
trace, with every value and normal included.

If \(A_N=A_N(w,t)\) has separate degree \(O(N)\) in an additional
real ordinary color \(w\), a uniform real bound for \(A_N\) gives
all fixed \(w\)-derivatives in (10) at polynomial cost, by Markov
before taking the trace. Uniform holomorphic parameter bounds give
the corresponding derivatives on smaller neighborhoods by Cauchy.
The output derivative assertion after (8) applies to (10) as well.
No parameter-dependent contour is differentiated.

For the actual next-three source, the
[exact dual observation, equation (30)](research_mixed_next_lowered_word_dual_observation.md) is
\[
 \mathcal F_{0,N}(w,Z)
       =\frac1{\kappa^3N}\,
             \mathfrak O_{-1,N}[\mathcal E_{33,N}(w,\cdot)](Z).
 \tag{11}
\]
Let \(M_{33}\) be the complete ordinary \(33\) action in
[its full boundary theorem](research_internal_pair_three_full_boundary_packet.md).
That theorem supplies
\(\sup_{w,t\in[-2,2]}|\mathcal E_{33,N}(w,t)|
\le CN^a e^{NM_{33}}\). Therefore (10) gives the genuine
whole-source upper bound
\[
 |\mathcal F_{0,N}(w,Z)|
   \le C_\tau N^{a_\tau}
       e^{N\{M_{33}+b_0+\log_+R+\tau\}},
 \quad w\in[-2,2],\quad |Z|\le R .
 \tag{12}
\]
The original \(\kappa^{-3}/N\) is already included in (11);
both parity cases and fixed ordinary/output jets are retained.

More usefully, if an exact polynomial error \(E_N(w,t)\) of
separate degrees \(O(N)\) has a global real bound
\[
 \|E_N\|_{\rm real}\le CN^a e^{N(M_{33}-\delta)},
 \tag{13}
\]
then its actual next-three observation has rate at most
\[
                   M_{33}-\delta+b_0+\log_+R+\tau .
 \tag{14}
\]
This is the explicit source-specific instance of calibrated
finite gluing. A local asymptotic error near \(t=-2\) is not an
input to (13). To pay (14) at the actual conditional action one
still needs, for example,
\[
 \Re\mathcal P_0^+(w,z)>
          M_{33}-\delta+b_0+\log_+R+\tau,
 \qquad |e^{-2\pi iz}|\le R .
 \tag{15}
\]
No inequality (15) is proved here. The available action floor
\(>2\) for an ordinary next three has not been identified with
the sum of the two separate rates in (14). Nor does (10) provide
a nonzero leading coefficient for the retained trace.

## 4. The exact inverse-crossing contour and its endpoint term

For \(N\ge3\), set
\[
 \begin{split}
 f_{N,w,Z}(t)
   &=\mathcal E_{33,N}(w,-2\cos t)
                       H_N(-2\cos t,rZ),\\
 g_{N,w,Z}(t)
   &=\sin t\, f_{N,w,Z}(t)e^{-iNt^2/(4\pi)},\\
 C_{N,-1}&=q^{-D^2/4},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \end{split}                                                   \tag{16}
\]
The function \(f\) is an even entire trigonometric polynomial.
Applying [the complete trace contour, Proposition 2](research_exact_complete_trace_contour.md)
with \(n=-1\) gives, for every fixed \(h>0\),
\[
 \boxed{\begin{split}
 \mathcal F_{0,N}(w,Z)
  ={}&-\frac{\kappa^{-3}NC_{N,-1}}{\pi i}
       \int_{-\pi-ih}^{\pi-ih}
                   g_{N,w,Z}(t)W_N(t)\,dt\\
    &+\frac{\eta\kappa^{-3}NC_{N,-1}}{\pi}
       \int_{-h}^{h}
          \frac{g_{N,w,Z}(\pi+iv)}
                         {4\cosh^2(Nv/2)}\,dv .
 \end{split}}                                                  \tag{17}
\]
The first path runs left to right. The second line is the exact
vertical endpoint current, with its sign and scalar. It is not
omitted or declared small. The square in \(W_N\) retains the
full normal contribution of every double spectral root.

In the lower half-plane,
\[
 W_N(t)=\sum_{\ell\ge1}\ell\eta^{\ell-1}e^{-i\ell Nt}.
 \tag{18}
\]
All these charges are already summed in (17). Moving the first
path inside the lower half-plane preserves the vertical term.
A principal-charge approximation would require a bound on the
whole deformed path; the local ordinary \(33\) expansion alone
does not supply it.

The existing whole-period bounds make the endpoint requirement
concrete. At complete left color write the ordinary \(33\) bound
as
\[
 |\mathcal E_{33,N}(-2,-2\cos(u+iv))|
   \le CN^a e^{N\{M_{33}-c_{33}(1-\cos u)+B_{33}v^2\}},
 \quad |v|\le h_{33},\quad c_{33}>0 .
 \tag{19}
\]
The endpoint polynomial in (8), as a trigonometric polynomial
in its ordinary color, has degree at most \(D\). Its whole real
bound therefore implies the exact strip bound
\[
 |H_N(-2\cos(u+iv),rZ)|
   \le C_\tau N^{a_\tau}
       e^{N\{b_0+\log_+R+\tau+|v|\}} .
 \tag{20}
\]
This follows from the disk maximum principle after multiplication
by the degree-\(D\) angular monomial, and evenness for the opposite
half-plane. It makes no new private-index continuation assumption.

On the endpoint line the inverse crossing in (16) has modulus
\(e^{Nv/2}\), while
\((4\cosh^2(Nv/2))^{-1}\le e^{-N|v|}\).
Thus the entire second line of (17), for \(0<h\le h_{33}\),
has the rigorous bound
\[
 C_{\tau,h}N^{a_{\tau,h}}
 \exp N\{M_{33}-2c_{33}+b_0+\log_+R+\tau
                                      +B_{33}h^2+h/2\}.
 \tag{21}
\]
The factor \(\sin(\pi+iv)\) is bounded on this fixed segment
and is retained in the exact formula. Bound (21) supplies a
sufficient endpoint comparison once its displayed rate is below
the intended action; that comparison is not assumed.

There is also a transparent limitation of using only these broad
strip bounds on the horizontal line. For \(t=u-ih\), the
endpoint polynomial costs \(e^{Nh}\), while \(W_N\) supplies
at most \(e^{-Nh}(1-e^{-Nh})^{-2}\). The remaining inverse-crossing
rate is \(-uh/(2\pi)\). Since
\(1-\cos u\ge2u^2/\pi^2\) for \(|u|\le\pi\), (19)--(20) give
the whole first-line rate at most
\[
 M_{33}+b_0+\log_+R+\tau
                +\left(B_{33}+\frac1{32c_{33}}\right)h^2 .
 \tag{22}
\]
The square completion proves the last term. In particular these
generic bounds do not themselves produce an exponential improvement
over (12) by lowering this contour. This is a limitation of the
displayed majorants, not a lower bound for the actual signed integral.
A sharper coupled source estimate or a proved cancellation in the
complete contour remains necessary.

The quotient inverse \(R_N^{-1}\) was never assigned a unit-modulus
bound on a complex contour. In (17) its exact physical crossing
data have instead been represented by the entire quadratic
exponential together with all trace charges and the vertical current.
No new full \(343\) packet or prescribed closing bound follows from
the upper estimates in this note.
