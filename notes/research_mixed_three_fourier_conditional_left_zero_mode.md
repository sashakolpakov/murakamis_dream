# The complete left half of the twice-crossed conditional zero mode

Research deduction, 7 November 2026. On the proved containing rectangle
for all actual type-three incoming references, the transformed
conditional critical point has strictly positive height. At that
height its original horizontal phase has a unique strict maximum on
the entire left half-period. This gives a nonzero Gaussian for that
whole path, and pays its left joining current relative to its own
conditional action.

The remaining right joining segment stays attached to the right
half-period. Neither its comparison nor the new conditional action's
comparison with the true endpoint forcing is inferred. No root,
analytic source, or numerical proposal is evaluated.

## 1. The critical height is positive on the actual-three input region

Use the original fixed \(y=x_0\) and the closed rectangle
\[
 \mathcal A=[267/1000,433/1000]+i[-9/125,17/250].
\tag{1}
\]
The
[actual-input theorem](research_mixed_three_conditional_actual_input_subdomain.md)
proves, for
\[
 P=\cot(\pi a)=p+i\alpha,\qquad
 Q=\cot(\pi y)=q+i\beta,
\]
that the original polynomial
\[
 F(S)=S^2+(P+Q)S-1+i(Q-P)
\tag{2}
\]
has exactly one simple root in
\(\Re S>0,\ |\Im S|<1\), with the original zero logarithmic lift.
Let \(s_*(a)\) be its original inverse cotangent.

The elementary witnesses of that theorem also give
\[
 p<\frac9{10},\qquad |\alpha|<\frac{387}{1000},\qquad
 q>\frac{127}{100},\qquad
            \frac{17}{25}<b:=-\beta<\frac{73}{100}.
\tag{3}
\]
Here are the two additional strict comparisons needed for (3).
At the smallest input real part, put \(\delta=17\pi/500\).
The previous witnesses give
\[
 \cos\delta<\frac{1243}{1250},\qquad
 \sin\delta>
   \frac{2669}{25000}-\frac{(187/1750)^3}{6}
                         >\frac{53}{500}.
\]
Since increasing the absolute input height can only decrease \(p\),
\[
 p\le\cot(267\pi/1000)
        <\frac{2486}{2765}<\frac9{10}.
\]
The bound for \(|\alpha|\) is the same monotone corner bound
used in equation (20) of the actual-input theorem. For the output,
\(\sinh(2\pi\Im y)>49/100\), while its cotangent denominator is
less than \(359/500\); hence
\[
                b>\frac{245}{359}>\frac{17}{25}.
\]
Thus (3) uses no new trigonometric or root evaluation.

**Lemma 1.** For every \(a\in\mathcal A\),
\[
                      h_*(a):=\Im s_*(a)>0.
\tag{4}
\]

*Proof.* Put \(c=b-\alpha\) and \(d=q-p\). The bounds (3) imply
\[
             0<c<9/8,\qquad d>37/100.
\]
Suppose the selected cotangent root were \(S=u+iv\) with \(v\ge0\).
The imaginary part of (2) gives
\[
             v=\frac{cu-d}{2u+p+q},\qquad
                         u\ge d/c,\quad 0\le v<c/2 .
\tag{5}
\]
Therefore \(cv-v^2\ge0\). The real part of (2) would satisfy
\[
 \begin{split}
 \Re F(S)
 &=u^2+(p+q)u+cv-v^2-1+\alpha+b\\
 &\ge\frac{d^2}{c^2}+\frac{q^2-p^2}{c}+2b-1-c\\
 &>\left(\frac{37}{100}\right)^2\frac{64}{81}
       +\frac{8029}{10000}\frac89+\frac9{25}-\frac98\\
 &=\frac{46054}{810000}>\frac1{20}>0.
 \end{split}
\tag{6}
\]
This contradicts \(F(S)=0\). Thus \(\Im S<0\), which is
equivalent to \(\Im s_*>0\) for the original inverse cotangent
on \(0<\Re s_*<1/2\). \(\square\)

Compactness and the already proved holomorphic simple branch make
\(h_*\) bounded above and bounded strictly away from zero on (1).
No explicit numerical height is required.

## 2. A strict maximum on the whole left half-period

Write the normalized conditional phase as
\[
 \mathscr F(s;a,y)
  =g(s+a)+g(s+y)-2g(s)-g(a)-g(y)+2\pi ias,
 \qquad \mathscr M(a)=\Re\mathscr F(s_*;a,y).
\tag{7}
\]
Every logarithm uses the original factorial continuation. Along
\(s=x+ih_*\), \(0\le x\le1/2\), the shifted real arguments
remain strictly between zero and one. At \(x=0\), the unshifted
factor uses its calibrated upper-half-plane continuation; \(h_*>0\)
keeps it away from its real zeros.

**Lemma 2.** The real phase in (7) strictly increases from \(x=0\)
to \(x=\Re s_*\), then strictly decreases to \(x=1/2\).
In particular it has a unique strict global maximum at \(s_*\), and
\[
                         \Re\{-\mathscr F_{ss}(s_*)\}>0.
\tag{8}
\]

*Proof.* The cotangent circle at positive height has the parametrization
\[
 \cot\pi(x+ih_*)=
       r_0\sin\theta-i(v_0+r_0\cos\theta),\qquad
 v_0=\coth(2\pi h_*)>1,\quad
 r_0=\operatorname{csch}(2\pi h_*),
\tag{9}
\]
where \(\theta\) increases strictly from zero to \(\pi\) as
\(x\) increases from zero to \(1/2\).
For the shift \(P=p+i\alpha\), set \(B_P=v_0-\alpha>0\).
Its squared distance is
\[
 |\cot\pi(x+ih_*)+P|^2
  =p^2+B_P^2+r_0^2
      +2r_0(p\sin\theta+B_P\cos\theta).
\tag{10}
\]
The analogous formula has \(q>0\) and \(B_Q=v_0-\beta>0\).
On \(0\le\theta\le\pi/2\), the second derivative of each
positive expression (10) is strictly negative. Its logarithm
is therefore strictly concave. On \(\pi/2\le\theta\le\pi\),
its first derivative is strictly negative.

The original critical identity gives exactly
\[
 f(\theta):=\partial_x\Re\mathscr F(x+ih_*;a,y)
   =\log\left|
      \frac{(\cot\pi(x+ih_*)+P)(\cot\pi(x+ih_*)+Q)}
           {(P-i)(Q+i)}\right|.
\tag{11}
\]
Thus \(f\) is strictly concave on the first angular quarter
and strictly decreasing on the second. At the selected root,
\(-1<\Im S_*<0\). Equation (9) implies \(\theta_*>\pi/2\);
also \(f(\theta_*)=0\) by the original logarithmic equation.
It follows that \(f(\pi/2)>0\).

At the left endpoint put \(C=\coth(\pi h_*)>1\).
The two ratios in (11) are separately greater than one:
\[
 |P-iC|>|P-i|,\qquad |Q-iC|>|Q+i|.
\tag{12}
\]
The first follows from \(\alpha<1\) and
\(C-\alpha>1-\alpha>0\); the second follows from \(\beta<0\)
and \(C-\beta>|1+\beta|\).
Hence \(f(0)>0\). Concavity now keeps \(f\) positive throughout
the first quarter. Strict decrease on the second gives precisely
one zero, at \(\theta_*\), with negative derivative there.
This proves both the sign pattern and (8). \(\square\)

All strict endpoint losses are uniform on the compact family (1).
This is a full horizontal-path comparison, not merely the local
nondegeneracy of the root.

## 3. The exact initial vertical line and its paid join

Use the same exact interpolant as in
[the complete endpoint-current theorem](research_mixed_three_fourier_conditional_endpoint_current.md):
\[
 T_N(s)=e^{2\pi iNas}
     \Pi_N(s+a)\Pi_N(s+y)E_N(a)E_N(y)E_N(s)^2.
\tag{13}
\]
The original Gamma product gives the useful all-level identity
\[
 \boxed{\qquad
 |E_N(iv)|^2=\frac1N\sum_{k=0}^{N-1}e^{2\pi kv},
                       \qquad v\in\mathbb R .
 \qquad}
\tag{14}
\]
To prove it, at the unscaled argument \(iNv\), the modulus squared
of each Gamma-product ratio is \(1+v^2/k^2\).
The identities
\[
 |\Gamma(1+iNv)|^2=\frac{\pi Nv}{\sinh(\pi Nv)},\qquad
 \prod_{k=1}^{\infty}(1+v^2/k^2)=\frac{\sinh(\pi v)}{\pi v}
\]
therefore give
\[
 |G_N(iNv)|^2=\frac{N\sinh(\pi v)}{\sinh(\pi Nv)}.
\]
Including the original marked phase yields
\[
 |\Pi_N(iv)|^2
       =\frac{N(e^{2\pi v}-1)}{e^{2\pi Nv}-1}.
\]
Its reciprocal is (14), including \(v=0\) by its limit.
In particular \(|E_N(iv)|^2\le e^{2\pi Nv}\) for \(v\ge0\).

Let \(L(v)\) be the original endpoint phase in (15) of the
endpoint-current theorem. Its all-height derivative bound is
\[
                    -2\pi(1-\Re y)<L'(v)<-2\pi\Re a.
\tag{15}
\]
For \(v\ge0\), \(\Re g_+(iv)=-\pi v\). Consequently
\[
 H_0(v):=\Re\mathscr F(iv;a,y)=L(v)+2\pi v,\qquad
 H_0'(v)>2\pi\Re y>0,\quad H_0(0)=0.
\tag{16}
\]
Lemma 2 gives \(H_0(h_*)<\mathscr M\). Thus
\[
       \mathscr M>H_0(h_*)>0
\tag{17}
\]
uniformly with strict margins on (1).
The regular numerator packets in (13), together with (14), give
the uniform finite bound
\[
 |T_N(iv)|\le C e^{NH_0(v)},\qquad 0\le v\le h_*.
\tag{18}
\]
There is no endpoint Stirling substitution at \(v=0\).
Thus the complete left join \(iN\int_0^{h_*}T_N(iv)\,dv\)
is exponentially smaller than \(e^{N\mathscr M}\).

The short interval \(\alpha_N=-1/(2N)\le s\le0\) also has
\[
                     N\left|\int_{\alpha_N}^0T_N(s)\,ds\right|
                                 \le C.
\tag{19}
\]
For its proof, the scaled real argument \(Ns\) belongs to
\([-1/2,0]\). The original Gamma product on that fixed interval
is a bounded nonzero multiple of
\((2\pi/N)^{Ns}\Gamma(1+Ns)\), uniformly in \(N\):
the logarithms of its remaining factors are \(O(N^{-2})\)
after their convergent \(k^{-2}\) sum.
Hence \(|E_N(s)|^2\le C N^{2Ns}\le C\).
The two shifted numerator-to-parameter factorial ratios and the
chirp in (13) are uniformly bounded on an interval of length
\(1/(2N)\). This proves (19).
By (17), (19) is also exponentially smaller than the new
conditional action.

## 4. The whole left path has a nonzero Gaussian

Define the complete horizontal path
\[
 I_N^{\rm L}=N\int_0^{1/2}T_N(u+ih_*)\,du.
\tag{20}
\]
With the original square-root continuation, put
\[
 \mathfrak a(z)=\sqrt{2\sin\pi z}\,e^{-\pi iz/2},\qquad
 A(s;a,y)=
    \frac{\mathfrak a(s+a)\mathfrak a(s+y)}
         {\mathfrak a(a)\mathfrak a(y)\mathfrak a(s)^2}.
\tag{21}
\]
The exact lower-half expansion and upper reflection give, uniformly
on a neighborhood of the whole path (20),
\[
             T_N(s)=N^{-1}A(s;a,y)e^{N\mathscr F(s;a,y)}
                                (1+O(N^{-1})).
\tag{22}
\]
At the unshifted left endpoint this uses the upper-half continuation
with its original phase. Every shifted numerator remains in the
regular real strip, so no shifted integer wall occurs on this path.
All factors of \(A\) are nonzero.

Lemma 2 supplies a strict whole-path gap away from the saddle,
uniform on (1), and (8) supplies its accretive Gaussian root.
Uniform stationary phase on the remaining neighborhood therefore
proves
\[
 \boxed{\quad
 I_N^{\rm L}
  =\sqrt{\frac{2\pi}{N}}\,
     \frac{A(s_*;a,y)}{\sqrt{-\mathscr F_{ss}(s_*;a,y)}}
          e^{N\mathscr F(s_*;a,y)}(1+O(N^{-1})).
 \quad}
\tag{23}
\]
The coefficient is nonzero. The first odd rescaled terms integrate
to zero; the remaining symbol and Gaussian errors give the displayed
relative order. Both parities use the same density \(N\) and
orientation. Formula (23) concerns the complete path (20), whose
height depends on the parameter; it is not a claim of holomorphic
derivatives of a parameter-dependent endpoint integral.

## 5. The exact remaining right path and the scope of the result

Let \(J_N\) be the complete paired endpoint current in equation (27)
of the endpoint-current theorem, and put
\[
 R_N=N\int_{1/2}^{\beta_N}T_N(u)\,du
                   -iN\int_0^{h_*}T_N(1/2+iv)\,dv .
\tag{24}
\]
This is one coherently retained path: it starts at
\(1/2+ih_*\), descends to \(1/2\), then runs right to \(\beta_N\).
The right vertical term is not estimated in isolation.
Exact contour orientation gives
\[
 \boxed{\quad
 C_{0,N}(X,e^{-2\pi iy})
       =I_N^{\rm L}+R_N+J_N+\mathcal E_N^{\rm L},
 \qquad
 \mathcal E_N^{\rm L}
       =N\int_{\alpha_N}^{0}T_N(u)\,du
                   +iN\int_0^{h_*}T_N(iv)\,dv .
 \quad}
\tag{25}
\]
No pole is crossed, because (13) is holomorphic on the complete
rectangle. By (17)--(19), there is a fixed \(\delta>0\) such that
\[
                  |\mathcal E_N^{\rm L}|
                         \le e^{N(\mathscr M(a)-\delta)}
\tag{26}
\]
for sufficiently large \(N\), uniformly on (1).
All original upper shifted-factor branches and possible numerator
zeros remain in \(R_N\).

The current \(J_N\) has already been bounded at the forcing rate
\(2\pi(-\Im a)_++2\pi\Im y\), and after the exact crossing
chirp/allocation it is paid relative to the old complete cap.
That is not a comparison of its rate with \(\mathscr M(a)\).
Neither \(R_N=o(I_N^{\rm L})\) nor
\(\mathscr M(a)>2\pi(-\Im a)_++2\pi\Im y\) is proved here.
Therefore (23)--(26) give a nonzero whole-left-path contribution
and a paid initial join, but do not yet identify a nonzero
asymptotic coefficient of the full conditional sum. Possible
competition or cancellation with the remaining right path
must still be resolved.
